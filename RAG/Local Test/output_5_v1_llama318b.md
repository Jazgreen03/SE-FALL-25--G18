**UC-01: Customer Places an Order**

* Preconditions:
        + The customer has created an account or is logged in as a guest.
        + The customer has added items to their cart.
        + The restaurant's menu and availability are displayed on the app.
* Main Flow:
        1. The customer views their cart and selects a payment method.
        2. The customer reviews their order summary, including the total cost and any applicable taxes or fees.
        3. The customer confirms their order and submits it for processing.
        4. The system sends an email confirmation to the customer with order details.
        5. The restaurant receives the order notification and begins preparing the food.
* Subflows:
        1A: Payment processing (step 1) - If payment fails, the app displays a payment failure message.
* Alternative Flows:
        Alt 3A: Order modification - If the customer attempts to modify their order after submitting it for processing.
**Assumptions:** None

**UC-02: Courier Views and Accepts an Assignment**

* Preconditions:
        + The courier has accepted terms of service and is logged in as a registered user.
        + The restaurant's delivery areas and assignment rules are set up in the system.
* Main Flow:
        1. The system displays available assignments for the courier, including order details and estimated delivery time.
        2. The courier reviews the assignment options and selects one to accept.
        3. The system sends a notification to the customer with the assigned courier's contact information.
        4. The courier confirms acceptance of the assignment via the app.
        5. The system updates the order status and triggers navigation for the courier to pick up the food.
* Subflows:
        2A: Assignment review (step 2) - If the courier declines an assignment, the system offers alternative options.
* Alternative Flows:
        Alt 3B: Courier cancellation - If the courier cancels their acceptance of the assignment after confirming it.

**UC-03: Restaurant Manages Orders and Inventory**

* Preconditions:
        + The restaurant has created an account or is logged in as a registered user.
        + The menu and inventory are set up in the system.
* Main Flow:
        1. The system displays available orders for the restaurant, including order details and status.
        2. The restaurant reviews orders and updates their status (e.g., "Preparing" to "Ready").
        3. The system sends notifications to the customer and courier with updated order status.
        4. The restaurant confirms delivery or cancellation of an order.
        5. The system updates inventory levels based on fulfilled orders.
* Subflows:
        1A: Order update (step 2) - If the restaurant updates an order's status, the app sends a notification to the customer and courier.

**UC-04: Admin/Support View and Manage System Data**

* Preconditions:
        + The admin/support user has access credentials and is logged in as an authorized user.
* Main Flow:
        1. The system displays dashboard data for orders, customers, restaurants, and couriers.
        2. The admin/support user views detailed reports on order history, customer demographics, and restaurant performance.
        3. The system allows the admin/support user to add or edit menu items, assign restaurants or couriers, and configure settings.
        4. The admin/support user reviews feedback and ratings from customers and responds accordingly.
* Alternative Flows:
        Alt 2A: System troubleshooting - If an error occurs while viewing reports.

**UC-05: Customer Views Order History and Reviews**

* Preconditions:
        + The customer has created an account or is logged in as a registered user.
* Main Flow:
        1. The system displays the customer's order history, including status and details.
        2. The customer views ratings and reviews from other customers for restaurants and couriers.
        3. The system allows the customer to leave feedback and ratings on orders.
        4. The app sends notifications with new review responses or updates.

Assumptions:

* All stakeholders (customer, courier, restaurant) have access to necessary hardware and internet connectivity.
* Data security measures are in place for sensitive information such as payment details.