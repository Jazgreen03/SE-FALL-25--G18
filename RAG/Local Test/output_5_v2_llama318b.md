**UC-01: Order Placement**

* Preconditions:
        + User has a registered account on the food delivery app.
        + User is logged in to their account.
        + User has searched for restaurants and selected a restaurant to order from.
* Main Flow:
        1. The user selects a restaurant and views its menu.
        2. The user adds items to their cart by selecting quantities and clicking "Add to Cart".
        3. The user proceeds to checkout by clicking the "Checkout" button.
        4. The user is prompted to enter their delivery address.
        5. The user confirms their order details, including total cost and estimated delivery time.
        6. The app processes the payment information using a secure payment gateway (e.g. Stripe).
        7. The app sends an order confirmation email to the user's registered email address.
        8. The app updates the restaurant's inventory and prepares for food preparation.

**UC-02: Order Tracking**

* Preconditions:
        + User has placed an order through the app.
        + Restaurant has started preparing the order.
* Main Flow:
        1. The app sends a confirmation email to the user with their order details, including estimated delivery time.
        2. As the restaurant prepares the order, the app updates the user's order status to "In Progress".
        3. When the driver is assigned to the order, the app sends an update to the user with the driver's name and contact information.
        4. The app tracks the order's progress in real-time as it is delivered by the driver.
        5. Once the order is delivered, the app updates the order status to "Delivered" and sends a notification to the user.

**UC-03: Rating and Review**

* Preconditions:
        + User has placed an order through the app and received their food.
        + Restaurant has been assigned to the order.
* Main Flow:
        1. The app prompts the user to rate their experience (e.g. 1-5 stars).
        2. The user provides a review of their experience, including comments about the restaurant and its staff.
        3. The app updates the restaurant's rating and review history.
        4. The app uses the user's feedback to improve future orders.

**UC-04: Restaurant Management**

* Preconditions:
        + User is an administrator or owner of the food delivery app.
        + Restaurant has been added to the app's database.
* Main Flow:
        1. The administrator logs in to their account and navigates to the restaurant management dashboard.
        2. The administrator updates the restaurant's menu, hours of operation, and other relevant information.
        3. The administrator assigns a driver or delivery partner to handle orders for the restaurant.
        4. The administrator monitors the restaurant's inventory and prepares for food preparation.

**UC-05: Payment Dispute**

* Preconditions:
        + User has placed an order through the app and experienced issues with payment processing.
        + Restaurant has been notified of the issue.
* Main Flow:
        1. The app detects a payment dispute (e.g. failed payment, cancelled credit card).
        2. The app notifies both the user and the restaurant of the issue.
        3. The app offers alternative payment methods or refunds as necessary.
        4. The app updates the order status to reflect the issue.

Assumptions:

* Secure payment processing is integrated with the app (e.g. Stripe, PayPal).
* Restaurant has a functioning inventory management system.
* User has a registered account and is logged in to their account at the time of ordering.