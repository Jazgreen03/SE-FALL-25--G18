import os, io, hashlib, pickle, faiss, numpy as np, argparse
from sentence_transformers import SentenceTransformer
from pathlib import Path
from PyPDF2 import PdfReader
import anthropic
from dotenv import load_dotenv
# ----------- Config -----------

PDF_DIR = "docs"
PAGE_FILE = "baeden_page.file"
CHUNK_WORDS = 180
TOPK = 6

load_dotenv()
#API_KEY=os.environ.get("ANTHROPIC_API_KEY")

# Claude model names
CLAUDE_MODELS = {
    "claude-haiku": "claude-3-haiku-20240307",
    "claude-sonnet": "claude-sonnet-4-20250514",
}

# Embedding model
#model = SentenceTransformer("all-Mini-L6-v2")
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
# ----------- PDF + Chunking -----------

def file_sig(path):
    p = Path(path)
    h = hashlib.md5()
    h.update(str(p.stat().st_mtime_ns).encode())
    h.update(str(p.stat().st_size).encode())
    return h.hexdigest()

def load_texts_with_meta(pdf_path):
    out = []
    p = Path(pdf_path)
    try:
        reader = PdfReader(str(p))
        for i, pg in enumerate(reader.pages, start=1):
            t = pg.extract_text() or ""
            if t.strip():
                out.append((t, {"doc": p.name, "page": i}))
    except Exception as e:
        print(f"warn: failed to read {p}: {e}")
    return out

def chunk_text(text, n=CHUNK_WORDS):
    w = text.split()
    return [" ".join(w[i:i+n]) for i in range(0, len(w), n)]

def build_chunks(pdf_dir):
    chunks, metas = [], []
    for pdf in Path(pdf_dir).glob("*.pdf"):
        for t, meta in load_texts_with_meta(pdf):
            cs = chunk_text(t)
            chunks.extend(cs)
            metas.extend([{**meta, "chunk": j+1} for j in range(len(cs))])
    return chunks, metas

# ----------- Indexing -----------

def encode(arr):
    return np.asarray(model.encode(arr, convert_to_numpy=True), dtype="float32")

def build_index(chunks):
    X = encode(chunks)
    ix = faiss.IndexFlatL2(X.shape[1])
    ix.add(X)
    return ix, X

def save_pagefile(ix, X, chunks, metas, manifest, path=PAGE_FILE):
    with open(path, "wb") as f:
        pickle.dump({"ix": ix, "X": X, "chunks": chunks, "metas": metas, "manifest": manifest}, f)

def load_pagefile(path=PAGE_FILE):
    with open(path, "rb") as f:
        return pickle.load(f)

# ----------- Index Updating -----------

def build_pagefile(pdf_dir=PDF_DIR, path=PAGE_FILE):
    chunks, metas = build_chunks(pdf_dir)
    ix, X = build_index(chunks)
    manifest = {str(p): file_sig(p) for p in Path(pdf_dir).glob("*.pdf")}
    save_pagefile(ix, X, chunks, metas, manifest, path)
    return ix, X, chunks, metas, manifest

def update_pagefile(pdf_dir=PDF_DIR, path=PAGE_FILE):
    if not os.path.exists(path):
        return build_pagefile(pdf_dir, path)
    pf = load_pagefile(path)
    old_manifest = pf["manifest"]
    current = {str(p): file_sig(p) for p in Path(pdf_dir).glob("*.pdf")}

    deleted = set(old_manifest) - set(current)
    added_or_changed = [p for p, s in current.items() if old_manifest.get(p) != s]

    if deleted:
        return build_pagefile(pdf_dir, path)

    if not added_or_changed:
        return pf["ix"], pf["X"], pf["chunks"], pf["metas"], current

    new_chunks, new_metas = [], []
    for p in added_or_changed:
        for t, meta in load_texts_with_meta(p):
            cs = chunk_text(t)
            new_chunks.extend(cs)
            new_metas.extend([{**meta, "chunk": j+1} for j in range(len(cs))])

    if new_chunks:
        X_new = encode(new_chunks)
        pf["ix"].add(X_new)
        pf["X"] = np.vstack([pf["X"], X_new])
        pf["chunks"].extend(new_chunks)
        pf["metas"].extend(new_metas)

    pf["manifest"] = current
    save_pagefile(pf["ix"], pf["X"], pf["chunks"], pf["metas"], pf["manifest"], path)
    return pf["ix"], pf["X"], pf["chunks"], pf["metas"], pf["manifest"]

# ----------- Claude RAG Query -----------

def query_rag(query, index, chunks, model_name, api_key, k=TOPK):
    qvec = encode([query])
    D, I = index.search(qvec, k)
    retrieved = [chunks[i] for i in I[0]]
    context = "\n\n".join(retrieved)

    prompt = f"""\
<|system|>
You are a helpful assistant tasked with helping create a new app.
<|user|>
You are assisting in the design of a food ordering and delivery system. You will generate a new use case based on the given title using structure and format below. This use cases must:

Follow the exact structure used in the examples (e.g., UC1, UC2, etc.).

Include sections: Preconditions, Main Flow, Subflows, and Alternative Flows.

Use clearly labeled subflows (e.g., [Display Menu]) and alternative flows (e.g., [AF1: Item Unavailable]).

Be inspired by the previous use cases (UC1–UC10), but should not simply repeat or slightly reword them.

Leverage additional domain knowledge that may exist in the supplemental PDFs (e.g., delivery logic, customer behavior, restaurant operations, etc.).

Please return your answer with clear use case identifiers (e.g., UC1 to UC15). Keep the writing consistent with the tone, clarity, and formatting of the original use cases.

Example:
UC1: Order a Drink as a Customer
Preconditions:
• The customer is logged in.
• At least one menu item is available.

Main Flow:
• The Customer opens the WolfCafe app or website.
• System displays available items [Display Menu].
• Customer selects one item [Select Item].
• Customer confirms selection [Place Order].
• The System confirms and submits the order [Confirm Order].

Subflows:
• [Display Menu] System retrieves and displays available items.
• [Select Item] Customer chooses an item from the list.
• [Place Order] Customer confirms (e.g., taps “Order Now”).
• [Confirm Order] System creates an order number, sets status to ORDERED, and shows a confirmation message.

Alternative Flows and Edge Cases:
• [AF1: No Available Items] At [Display Menu], if no items are available show: “Sorry, no items are currently available.” and return to start.
• [AF2: Item Unavailable After Selection] At [Place Order], if the item is no longer available show: “Sorry, that item just sold out.” and return to [Display Menu].

Context:
{context}

Question: {query}

Answer:"""

    client = anthropic.Anthropic(api_key=api_key)
    resp = client.messages.create(
        model=model_name,
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    return resp.content[0].text, list(zip(D[0].tolist(), I[0].tolist()))

# ----------- Helpers -----------

def show_page_table(chunks, metas, scores):
    print("# Semantic Page Table (top-k)")
    for r, (d, idx) in enumerate(scores, 1):
        m = metas[idx]
        snip = chunks[idx][:80].replace('\n', ' ')
        print(f"{r:>2}. idx={idx:>6}  L2^2={d:.4f}  {m['doc']}#p{m['page']}  '{snip}'")

def ensure_pagefile():
    return update_pagefile(PDF_DIR, PAGE_FILE)

# ----------- Main CLI -----------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="RAG with Claude Haiku or Sonnet")
    parser.add_argument("--query", type=str, help="Single question to ask")
    parser.add_argument("--input", type=str, help="Path to text file with one query per line")
    parser.add_argument("--output", type=str, default="results.txt", help="Output file to save answers")
    parser.add_argument("--model", choices=["claude-haiku", "claude-sonnet"], default="claude-sonnet", help="Claude model")
    parser.add_argument("--api-key", type=str, default=os.getenv("ANTHROPIC_API_KEY"), help="Anthropic API key")
    args = parser.parse_args()

    if not args.api_key:
        raise ValueError("Anthropic API key required. Use --api-key or set ANTHROPIC_API_KEY env variable.")

    # Load or update index
    ix, X, chunks, metas, manifest = ensure_pagefile()
    model_id = CLAUDE_MODELS[args.model]

    # Collect queries
    if args.input:
        with open(args.input, "r", encoding="utf-8") as f:
            queries = [line.strip() for line in f if line.strip()]
#            full_query = f.read().strip()
#            queries = [full_query]
    elif args.query:
        queries = [args.query]
    else:
        raise ValueError("Provide a --query or --input file.")

    # Run batch
    results = []
    for i, q in enumerate(queries, 1):
        print(f"\n🔍 Query {i}/{len(queries)}: {q}")
        try:
            answer, scores = query_rag(q, ix, chunks, model_id, args.api_key, k=TOPK)
            show_page_table(chunks, metas, scores)
            print(f"\n📥 Answer:\n{answer}\n")
            results.append(f"Q{i}: {q}\nA{i}: {answer}\n{'-'*60}\n")
        except Exception as e:
            print(f"❌ Error on query {i}: {e}")
            results.append(f"Q{i}: {q}\nA{i}: [ERROR: {e}]\n{'-'*60}\n")

    # Write output file
    with open(args.output, "w", encoding="utf-8") as f:
        f.writelines(results)

    print(f"\n✅ Saved {len(results)} answers to: {args.output}")

