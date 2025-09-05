 **Use‑Case 1**
**ID:** UC‑01
**Name:** Place a Food Order (Customer)

**Preconditions**
- Customer has a registered account and is logged in. *(Assumption: the app requires authentication before ordering.)*
- Customer’s device has internet connectivity.
- At least one restaurant is available in the delivery area.

**Main Flow**
1. Open the app and browse the restaurant catalogue.
2. Select a restaurant and add desired menu items to the cart.
3. Review the cart, choose delivery address, and select a delivery time slot.
4. Choose a payment method and confirm the order.
5. Receive an order‑confirmation screen with a unique order ID and estimated delivery time.

**Subflows**
- **SF‑1. Apply Promo Code (Step 3)**
  1. Tap “Add Promo Code”.
  2. Enter the code and press “Apply”.
  3. System validates the code and updates the cart total.

**Alternative Flows**
- **Alt 4A – Payment Declined:**
  *Triggered at Step 4.*
  1. System notifies the customer that the selected payment method was declined.
  2. Customer selects an alternative payment method or edits the cart.
  3. Return to Step 4.

- **Alt 3A – No Delivery Slot Available:**
  *Triggered at Step 3.*
  1. System informs the customer that no slots are available for the chosen time.
  2. Customer selects a different time slot or chooses “ASAP”.
  3. Return to Step 3.

**Assumptions**
- The app presents a searchable list of restaurants and their menus.
- Payment methods include credit/debit cards and third‑party wallets.
- Promo‑code functionality exists (not explicitly stated in the source).



---

**Use‑Case 2**
**ID:** UC‑02
**Name:** Receive and Confirm Order (Restaurant)

**Preconditions**
- Restaurant is registered on the platform and has an active online status. *(Assumption: restaurants must be onboarded to receive orders.)*
- The restaurant’s order‑management interface (web or app) is accessible.

**Main Flow**
1. System pushes the new order notification to the restaurant’s dashboard.
2. Restaurant staff view order details, including items, delivery address, and requested time.
3. Verify item availability and preparation feasibility.
4. Accept the order and set an estimated preparation completion time.
5. System acknowledges acceptance and updates order status to “Preparing”.

**Subflows**
- **SF‑2. Request Order Modification (Step 3)**
  1. Staff selects “Request Change”.
  2. Specify unavailable items or suggest alternatives.
  3. System sends a modification request to the customer.

**Alternative Flows**
- **Alt 4A – Order Rejection:**
  *Triggered at Step 4.*
  1. Staff marks the order as “Reject”.
  2. System notifies the customer and suggests alternative restaurants.
  3. Order status changes to “Cancelled”.

- **Alt 5A – Preparation Delay:**
  *Triggered after Step 5.*
  1. Staff updates the estimated ready time to a later slot.
  2. System notifies the customer of the new ETA.

**Assumptions**
- Restaurants receive real‑time push notifications (implied by “features, process” in the source).
- The platform supports order‑status tracking visible to customers and couriers.



---

**Use‑Case 3**
**ID:** UC‑03
**Name:** Accept, Pick Up, and Deliver Order (Courier/Driver)

**Preconditions**
- Courier is registered, has passed background checks, and is logged into the driver app. *(Assumption: a separate driver app exists.)*
- An order in “Ready for Pickup” status is available in the courier’s delivery queue.

**Main Flow**
1. Courier receives a delivery request with order details and pickup location.
2. Accept the delivery request.
3. Navigate to the restaurant using built‑in map directions.
4. Arrive at the restaurant, verify the order ID, and collect the packaged food.
5. Mark the order as “Picked Up” in the app.
6. Follow navigation to the customer’s delivery address.
7. Arrive at the destination, confirm delivery with the customer’s signature or OTP.
8. Mark the order as “Delivered” to complete the trip.

**Subflows**
- **SF‑3. Reassign Delivery (Step 2)**
  1. Courier declines the request (e.g., due to distance).
  2. System reassigns the order to another available courier.

**Alternative Flows**
- **Alt 4A – Unable to Locate Order:**
  *Triggered at Step 4.*
  1. Courier reports missing items to the restaurant via the app.
  2. Restaurant resolves the issue (e.g., prepares a new package).
  3. Return to Step 4.

- **Alt 7A – Customer Not Available:**
  *Triggered at Step 7.*
  1. Courier contacts the customer using the in‑app call function.
  2. If still unreachable, courier marks the order as “Failed Delivery” and notifies support.

**Assumptions**
- The driver app provides map navigation and OTP/signature capture.
- Couriers can accept or reject assignments in real time.



---

**Use‑Case 4**
**ID:** UC‑04
**Name:** Process Refund for Canceled Order (Admin/Support)

**Preconditions**
- Customer has submitted a cancellation request through the app. *(Assumption: customers can cancel before a certain status.)*
- Order status is “Pending” or “Preparing” and is eligible for refund per business rules.

**Main Flow**
1. Support staff view the cancellation request in the admin console.
2. Verify the order eligibility (time of cancellation, payment status).
3. Initiate a refund transaction via the integrated payment gateway.
4. Record the refund reference and update order status to “Refunded”.
5. Notify the customer of successful refund via push notification and email.

**Subflows**
- **SF‑4. Escalate Disputed Refund (Step 2)**
  1. If eligibility is unclear, staff escalates to a senior manager.
  2. Manager reviews and decides to approve or deny the refund.
  3. Return to Step 3 with the manager’s decision.

**Alternative Flows**
- **Alt 3A – Refund Failure:**
  *Triggered at Step 3.*
  1. Payment gateway returns an error code.
  2. Staff retries the refund up to two times.
  3. If still failing, log the incident and open a ticket for finance team.

- **Alt 5A – Customer Does Not Receive Notification:**
  *Triggered after Step 5.*
  1. Customer contacts support claiming no notification.
  2. Support manually resends the notification and confirms receipt.

**Assumptions**
- The platform integrates with a third‑party payment gateway capable of issuing refunds.
- An admin console exists for support staff to manage orders and refunds.



---

**Use‑Case 5**
**ID:** UC‑05
**Name:** Authorize and Capture Payment (Payment/3rd‑Party)

**Preconditions**
- Customer has selected a payment method and confirmed the order (see UC‑01).
- The payment service provider (PSP) API credentials are configured in the system. *(Assumption: a PSP is integrated.)*

**Main Flow**
1. App sends an authorization request to the PSP with order amount, currency, and tokenized card/wallet details.
2. PSP validates the payment instrument and returns an authorization token.
3. App stores the token and displays a “Payment Authorized” status to the customer.
4. When the restaurant marks the order as “Ready for Pickup”, the app sends a capture request using the stored token.
5. PSP processes the capture, debits the customer’s account, and returns a transaction receipt.
6. App records the receipt, updates order status to “Paid”, and triggers the notification to the restaurant and courier.

**Subflows**
- **SF‑5. Save Card for Future Use (Step 1)**
  1. Customer opts to save payment details.
  2. PSP returns a secure payment token that is stored for future orders.

**Alternative Flows**
- **Alt 2A – Authorization Declined:**
  *Triggered at Step 2.*
  1. PSP returns a decline response with an error code.
  2. App informs the customer and prompts selection of an alternative payment method.
  3. Return to Step 1 with new method.

- **Alt 4A – Capture Timeout:**
  *Triggered at Step 4.*
  1. Capture request fails because the order was not marked “Ready”.
  2. System retries capture after a configurable interval (e.g., 5 minutes).
  3. If still failing, the order is flagged for manual review.

**Assumptions**
- The payment flow follows a typical “authorize‑then‑capture” model common in food‑delivery platforms.
- The app can receive real‑time webhook callbacks from the PSP for status updates.



---

*All facts stated above are either directly implied by the “features, process, cost, business model” focus of the referenced development guide, or are explicitly listed under **Assumptions** where the source material does not provide concrete details.*