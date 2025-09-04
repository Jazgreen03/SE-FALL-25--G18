import os, io, hashlib, pickle, faiss, numpy as np
from sentence_transformers import SentenceTransformer
from pathlib import Path
from PyPDF2 import PdfReader
from dotenv import load_dotenv
import requests

load_dotenv()
apiKey = os.getenv("OPENAI_API_KEY")

PDF_DIR = "docs"
PAGE_FILE = "page.file"
CHUNK_WORDS = 220       # ≈ short paragraph (150–220 works well)
TOPK = 8                # sensible default (5–8)

model = SentenceTransformer("multi-qa-mpnet-base-dot-v1")

# ---- Local LLM (Ollama) helper ----
def chat_local_ollama(prompt, model=None, url=None):
    """
    Calls a local Ollama server (default http://localhost:11434) using its /api/chat endpoint.
    """
    url = url or os.getenv("OLLAMA_URL")
    model = model or os.getenv("OLLAMA_MODEL")
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False
    }
    r = requests.post(f"{url}/api/chat", json=payload)
    r.raise_for_status()
    data = r.json()
    return data["message"]["content"]

def load_query(path="query.md"):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    # Fallback if no file is present
    return ("Generate 10 Use Cases for a consumer Food Delivery application "
            "following the specified structure (Preconditions, Main Flow, Subflows, "
            "Alternative Flows), grounded strictly in the provided context.")

def build_prompt(context, query_text):
    return (
        f"{query_text}\n\n"
        "REFERENCE CONTEXT (top-k retrieved snippets)\n"
        "-------------------------------------------\n"
        f"{context}\n"
    )


def file_sig(path):
    p=Path(path); h=hashlib.md5()
    h.update(str(p.stat().st_mtime_ns).encode()); h.update(str(p.stat().st_size).encode())
    return h.hexdigest()

def load_texts_with_meta(pdf_path):  # -> list[(text, meta)] where meta has doc/page
    out=[]; p=Path(pdf_path)
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
    w=text.split(); return [" ".join(w[i:i+n]) for i in range(0,len(w),n)]

def build_chunks(pdf_dir):
    chunks, metas = [], []
    for pdf in Path(pdf_dir).glob("*.pdf"):
        for t, meta in load_texts_with_meta(pdf):
            cs = chunk_text(t)
            chunks.extend(cs)
            metas.extend([{**meta, "chunk": j+1} for j in range(len(cs))])
    return chunks, metas

def encode(arr):
    return np.asarray(model.encode(arr, convert_to_numpy=True), dtype="float32")

def build_index(chunks):
    X = encode(chunks)
    ix = faiss.IndexFlatL2(X.shape[1])  # squared L2 distance
    ix.add(X)
    return ix, X

def save_pagefile(ix, X, chunks, metas, manifest, path=PAGE_FILE):
    with open(path, "wb") as f:
        pickle.dump({"ix": ix, "X": X, "chunks": chunks, "metas": metas,
                     "manifest": manifest}, f)

def load_pagefile(path=PAGE_FILE):
    with open(path, "rb") as f: return pickle.load(f)

# Build fresh (first run)

def build_pagefile(pdf_dir=PDF_DIR, path=PAGE_FILE):
    chunks, metas = build_chunks(pdf_dir)
    ix, X = build_index(chunks)
    manifest = {str(p): file_sig(p) for p in Path(pdf_dir).glob("*.pdf")}
    save_pagefile(ix, X, chunks, metas, manifest, path)
    return ix, X, chunks, metas, manifest

# Update (incremental add/modify). If deletions detected → rebuild for simplicity.

def update_pagefile(pdf_dir=PDF_DIR, path=PAGE_FILE):
    if not os.path.exists(path):
        return build_pagefile(pdf_dir, path)
    pf = load_pagefile(path)
    old_manifest = pf["manifest"]
    current = {str(p): file_sig(p) for p in Path(pdf_dir).glob("*.pdf")}

    deleted = set(old_manifest) - set(current)
    added_or_changed = [p for p,s in current.items() if old_manifest.get(p) != s]

    if deleted:
        # IndexFlatL2 lacks easy deletions; simplest: full rebuild to stay correct.
        return build_pagefile(pdf_dir, path)

    if not added_or_changed:
        return pf["ix"], pf["X"], pf["chunks"], pf["metas"], current

    # Append new/changed content
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

def query_rag(query, index, chunks, k=TOPK):
    qvec = encode([query])
    D, I = index.search(qvec, k)           # D: squared distances, I: indices
    retrieved = [chunks[i] for i in I[0]]
    context = "\n\n".join(retrieved)
    prompt = build_prompt(context, query)
    answer = chat_local_ollama(prompt)
    return answer, list(zip(D[0].tolist(), I[0].tolist()))

def show_page_table(chunks, metas, scores):
    print("# Semantic Page Table (top-k)")
    for r,(d, idx) in enumerate(scores, 1):
        m = metas[idx]
        snip = chunks[idx][:80].replace('\n',' ')
        print(f"{r:>2}. idx={idx:>6}  L2^2={d:.4f}  {m['doc']}#p{m['page']}  '{snip}'")

def ensure_pagefile():
    return update_pagefile(PDF_DIR, PAGE_FILE)

if __name__ == "__main__":
    ix,X,chunks,metas,manifest = ensure_pagefile()
    query_text = load_query("query.md")
    ans, scores = query_rag(query_text, ix, chunks, k=TOPK)
    show_page_table(chunks, metas, scores)
    print("\n---\n", ans)