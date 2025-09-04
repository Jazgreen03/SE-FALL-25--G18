**Use‑Case 1 – UC‑01 – “Customer Places an Order”**  

| Element | Description |
|---|---|
| **Preconditions** | • The customer has installed the food‑delivery mobile app and is logged in.<br>• The device has an active internet connection.<br>• At least one restaurant is available in the customer’s delivery zone (assumed from typical food‑delivery services). |
| **Main Flow** | 1. **Search Restaurants** – Customer enters a delivery address and browses the list of nearby restaurants.<br>2. **Select Restaurant & Menu Items** – Customer chooses a restaurant, views its menu, and adds desired dishes to the cart.<br>3. **Review Cart** – Customer opens the cart, verifies items, quantities, and sees the subtotal, delivery fee, and estimated taxes.<br>4. **Enter Delivery Details** – Customer confirms the delivery address (or selects a saved one) and adds optional delivery instructions.<br>5. **Proceed to Payment** – Customer taps *Checkout* to move to the payment screen. |
| **Sub‑flows** | **SF‑1 – Add/Remove Items** (from Step 2):<br> 1. Customer taps “+” or “–” beside an item.<br> 2. System updates cart total instantly.<br>**SF‑2 – Save Favorite Order** (from Step 4):<br> 1. Customer selects “Save as favorite”.<br> 2. System stores the order template in the user profile. |
| **Alternative Flows** | **Alt 5A – Payment Method Not Available** – If the selected payment method is unsupported for the order total, system returns to Step 5 and prompts the customer to choose another method.<br>**Alt 2A – Restaurant Out of Stock** – While adding an item, system notifies “Out of stock” and returns to Step 2. |
| **Assumptions** | • The app provides searchable restaurant listings and menu browsing (derived from “features” of a typical food‑delivery app).<br>• Delivery fee and tax calculation are performed automatically (not described in the context). |     

---

**Use‑Case 2 – UC‑02 – “Restaurant Receives & Confirms Order”**

| Element | Description |
|---|---|
| **Preconditions** | • The restaurant has a registered account on the platform and is logged into the restaurant‑partner portal (web or app).<br>• The restaurant’s operating hours are active and the kitchen is ready to accept orders. |
| **Main Flow** | 1. **Order Notification** – System pushes a new order alert to the restaurant’s dashboard.<br>2. **View Order Details** – Restaurant staff opens the order to see items, quantities, special instructions, and delivery address.<br>3. **Validate Availability** – Staff checks inventory and confirms that all items can be prepared.<br>4. **Accept Order** – Staff taps *Accept*; system timestamps the acceptance and sends a confirmation to the customer.<br>5. **Start Preparation** – Kitchen begins cooking; system updates order status to *Preparing*. |
| **Sub‑flows** | **SF‑1 – Request Modification** (from Step 3):<br> 1. Staff selects “Request Change”.<br> 2. System sends a modification request to the customer.<br> 3. Customer approves or declines; if approved, system updates the order and returns to Step 3. |
| **Alternative Flows** | **Alt 4A – Order Rejection** – If the restaurant cannot fulfil the order, staff taps *Reject*; system notifies the customer, re‑queues the order to other nearby restaurants, and logs the rejection.<br>**Alt 5A – Preparation Delay** – If preparation exceeds a defined threshold, system escalates to Admin (see UC‑05). |
| **Assumptions** | • Restaurants receive real‑time push notifications (standard in delivery platforms).<br>• Order status flow includes *New → Accepted → Preparing → Ready for Pickup* (inferred from typical processes). |

---

**Use‑Case 3 – UC‑03 – “Courier Accepts & Picks Up Order”**

| Element | Description |
|---|---|
| **Preconditions** | • Courier/driver has a verified driver account and is logged into the driver app.<br>• Courier is within the service area and has an active shift (available status). |
| **Main Flow** | 1. **Receive Delivery Assignment** – System sends a push notification with order details (restaurant, pickup time, distance).<br>2. **Accept Assignment** – Courier taps *Accept*; system records acceptance time and updates order status to *Courier Assigned*.<br>3. **Navigate to Restaurant** – Driver opens built‑in map, follows navigation to the restaurant.<br>4. **Pick Up Order** – Upon arrival, driver confirms pickup; system changes status to *Picked Up* and notifies the customer.<br>5. **Deliver to Customer** – Driver follows navigation to the delivery address, marks *Delivered* on arrival, and optionally captures a photo signature. |
| **Sub‑flows** | **SF‑1 – En‑route Delay** (from Step 3):<br> 1. Driver reports traffic delay.<br> 2. System updates estimated arrival time and notifies the customer. |
| **Alternative Flows** | **Alt 2A – Assignment Decline** – If courier declines, system re‑assigns the order to the next available driver and logs the decline.<br>**Alt 4A – Pickup Failure** – If the restaurant reports the order is not ready, driver can request a *Reschedule*; system updates the expected pickup time.<br>**Alt 5A – Delivery Failure** – If the customer is unreachable, driver marks *Attempted Delivery*; system creates a support ticket (see UC‑05). |
| **Assumptions** | • Driver app includes map/navigation and status update capabilities (common in delivery solutions).<br>• Photo signature or proof‑of‑delivery is optional but supported (assumed for order verification). |

---

**Use‑Case 4 – UC‑04 – “Customer Completes Payment via 3rd‑Party Gateway”**

| Element | Description |
|---|---|
| **Preconditions** | • Customer has reached the *Checkout* screen with a finalized order (from UC‑01).<br>• Customer’s chosen payment method (card, digital wallet, etc.) is linked to a supported 3rd‑party payment processor. |
| **Main Flow** | 1. **Select Payment Method** – Customer chooses a saved card, digital wallet, or adds a new method.<br>2. **Enter Payment Details** – If a new method, customer inputs card number, expiry, CVV, and billing address.<br>3. **Submit Payment** – Customer taps *Pay Now*; app sends a payment request to the 3rd‑party gateway.<br>4. **Gateway Authorization** – Payment gateway processes the transaction and returns *Authorized* or *Declined*.<br>5. **Confirm Order** – On *Authorized*, system records payment, updates order status to *Paid*, and sends confirmation to the customer, restaurant, and courier. |      
| **Sub‑flows** | **SF‑1 – Save New Payment Method** (from Step 2):<br> 1. Customer checks “Save for future orders”.<br> 2. System stores tokenized payment data securely. |
| **Alternative Flows** | **Alt 4A – Payment Declined** – If the gateway returns *Declined*, system displays an error, returns to Step 1, and allows the customer to choose a different method.<br>**Alt 3A – Network Timeout** – If the request to the gateway times out, system retries up to 2 times; on final failure, it notifies the customer and logs the incident for support. |
| **Assumptions** | • The platform integrates with at least one external payment processor (standard in “Payment/3rd‑party perspective”).<br>• Payment data is tokenized and stored securely according to PCI‑DSS (implied best practice). |

---

**Use‑Case 5 – UC‑05 – “Admin Handles Customer Support Ticket (Order Dispute)”**

| Element | Description |
|---|---|
| **Preconditions** | • A support ticket has been automatically generated (e.g., delivery failure, payment issue) or manually created by the customer via the *Help* section.<br>• Admin/support staff is logged into the admin console with appropriate privileges. |
| **Main Flow** | 1. **View Ticket Queue** – Admin opens the support dashboard and sees a list of open tickets.<br>2. **Select Ticket** – Admin clicks on a specific ticket to view details (order ID, customer notes, timestamps).<br>3. **Investigate** – Admin reviews order history, payment logs, courier tracking, and any attached photos.<br>4. **Take Action** – Admin chooses an action: issue refund, reorder, or contact courier/restaurant.<br>5. **Communicate Outcome** – System sends a status update to the customer (e.g., “Refund issued”) and logs the action for audit. |
| **Sub‑flows** | **SF‑1 – Escalate to Management** (from Step 4):<br> 1. Admin selects *Escalate*.<br> 2. System forwards ticket to senior manager and marks it as *Pending Review*. |
| **Alternative Flows** | **Alt 3A – Insufficient Information** – If required logs are missing, admin adds a note requesting additional data from the courier/restaurant; ticket status changes to *Awaiting Info*.<br>**Alt 4A – Refund Failure** – If the refund request to the payment gateway fails, system notifies admin and offers to retry or issue a manual credit. |
| **Assumptions** | • The platform generates support tickets automatically for critical failures (delivery missed, payment declined after order placed).<br>• Admin console provides full visibility into order, payment, and courier data (standard for operational back‑ends). |

---

**Summary of Perspectives Covered**

| Use‑Case | Primary Perspective |
|---|---|
| UC‑01 | Customer |
| UC‑02 | Restaurant (partner) |
| UC‑03 | Courier / Driver |
| UC‑04 | Payment / 3rd‑Party Gateway |
| UC‑05 | Admin / Support |

All facts are either drawn from the generic “features, process” notion in the reference snippets or explicitly marked as **Assumptions** where the context did not specify the detail.