You are a software developer. Use ONLY the reference context below. 
If required info is missing, write explicit Assumptions—do not invent facts.

TASK
Generate 15 unique and detailed Use Cases for a consumer Food Delivery application.

OUTPUT FOR EACH USE CASE
- ID: UC-##
- Name
- Preconditions (bulleted)
- Main Flow (numbered, > 3 steps, imperative voice)
- Subflows (if any; numbered; reference from Main Flow steps)
- Alternative Flows (edge/error paths; tie back to specific Main Flow steps)
- Assumptions (ONLY if context lacks specifics)

CONSTRAINTS
- Cover Customer, Courier/Driver, Restaurant, Admin/Support, and Payment/3rd-party systems across the 15 Use Cases.
- Keep each Use Case ≤ 300 tokens.
- Ground every stated fact in the context or list it under Assumptions.

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