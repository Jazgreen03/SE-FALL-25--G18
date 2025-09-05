### Use Case 1
- **ID:** UC-01
- **Name:** Customer Login
- **Preconditions:**
  - Customer has an existing account.
- **Main Flow:**
  1. Customer opens the food delivery app.
  2. Customer navigates to the login screen.
  3. Customer inputs username and password.
  4. Customer clicks "Login."
  5. System validates credentials.
  6. System redirects customer to the homepage.
- **Subflows:** None.
- **Alternative Flows:**
  - **Alt 3A:** Incorrect credentials prompt an error message.
- **Assumptions:** Customer remembers their login credentials.

### Use Case 2
- **ID:** UC-02
- **Name:** Place Order
- **Preconditions:**
  - Customer is logged in.
  - Restaurant is available for orders.
- **Main Flow:**
  1. Customer browses available restaurants.
  2. Customer selects a restaurant.
  3. Customer picks items from the menu.
  4. Customer adds items to the cart.
  5. Customer confirms the order.
  6. System processes the order.
- **Subflows:** None.
- **Alternative Flows:**
  - **Alt 5A:** Out-of-stock items prompt customer to modify order.
- **Assumptions:** Customer has an active internet connection.

### Use Case 3
- **ID:** UC-03
- **Name:** Choose Payment Method
- **Preconditions:**
  - Customer has items in the cart.
- **Main Flow:**
  1. Customer proceeds to checkout.
  2. Customer selects a payment method (credit card, cash).
  3. System displays payment information based on the method chosen.
  4. Customer fills in the required details.
  5. Customer confirms payment method.
- **Subflows:** None.
- **Alternative Flows:**
  - **Alt 4A:** Payment method validation fails.
- **Assumptions:** Customer has valid payment information.

### Use Case 4
- **ID:** UC-04
- **Name:** Track Order Status
- **Preconditions:**
  - Customer has placed an order.
- **Main Flow:**
  1. Customer accesses the order status screen.
  2. System displays current status of the order.
  3. Customer can view estimated delivery time.
  4. Customer receives notifications on any status changes.
- **Subflows:** None.
- **Alternative Flows:**
  - **Alt 3A:** System returns an error if the order ID is invalid.
- **Assumptions:** System tracks orders accurately.

### Use Case 5
- **ID:** UC-05
- **Name:** Cancel Order
- **Preconditions:**
  - Customer has an active order.
- **Main Flow:**
  1. Customer navigates to the order history.
  2. Customer selects the active order to cancel.
  3. Customer indicates the reason for cancellation.
  4. System processes the cancellation.
  5. Customer receives confirmation of cancellation.
- **Subflows:** None.
- **Alternative Flows:**
  - **Alt 4A:** Cancellation fails as the order is already in transit.
- **Assumptions:** Customer understands cancellation policy.

### Use Case 6
- **ID:** UC-06
- **Name:** Rate and Review Restaurant
- **Preconditions:**
  - Customer has made at least one order from the restaurant.
- **Main Flow:**
  1. Customer navigates to the restaurant page.
  2. Customer clicks on "Rate and Review."
  3. Customer selects a star rating and writes a review.
  4. Customer submits the review.
  5. System records the review and updates average rating.
- **Subflows:** None.
- **Alternative Flows:**
  - **Alt 3A:** Review submission fails due to inappropriate content.
- **Assumptions:** Customer has an opinion about the restaurant.

### Use Case 7
- **ID:** UC-07
- **Name:** Register New Account
- **Preconditions:**
  - Customer is not logged in.
- **Main Flow:**
  1. Customer opens the app.
  2. Customer selects "Sign Up."
  3. Customer inputs required details (name, email, password).
  4. Customer submits the registration form.
  5. System creates a new account and logs the customer in.
- **Subflows:** None.
- **Alternative Flows:**
  - **Alt 4A:** Email already in use prompts the customer to log in instead.
- **Assumptions:** Customer has valid information to register.

### Use Case 8
- **ID:** UC-08
- **Name:** Login via Social Media
- **Preconditions:**
  - Customer has a social media account linked.
- **Main Flow:**
  1. Customer opens the app.
  2. Customer selects "Login with [Social Media]."
  3. System redirects to social media authentication.
  4. Customer approves permissions.
  5. System creates or accesses the account and logs the customer in.
- **Subflows:** None.
- **Alternative Flows:**
  - **Alt 3A:** Cancellation of permissions results in login failure.
- **Assumptions:** Customer is already logged into social media on the device.

### Use Case 9
- **ID:** UC-09
- **Name:** Update Profile Information
- **Preconditions:**
  - Customer is logged in.
- **Main Flow:**
  1. Customer navigates to the profile section.
  2. Customer edits personal information (name, address).
  3. Customer submits changes.
  4. System updates profile information.
  5. System confirms changes via notification.
- **Subflows:** None.
- **Alternative Flows:**
  - **Alt 3A:** Changes fail due to validation errors.
- **Assumptions:** Customer wants to keep their profile current.

### Use Case 10
- **ID:** UC-10
- **Name:** Refund for Incorrect Order
- **Preconditions:**
  - Customer has received an incorrect item.
- **Main Flow:**
  1. Customer navigates to order history.
  2. Customer selects the incorrect order.
  3. Customer reports the issue via “Report Problem.”
  4. System prompts for refund or replacement choice.
  5. Customer submits request.
  6. System processes the refund or schedules a replacement.
- **Subflows:** None.
- **Alternative Flows:**
  - **Alt 5A:** Refund request is denied due to policy restrictions.
- **Assumptions:** Customer understands the refund policies.

### Use Case 11
- **ID:** UC-11
- **Name:** Assign Courier to Order
- **Preconditions:**
  - Admin or system is processing orders.
- **Main Flow:**
  1. Admin views incoming orders.
  2. Admin selects an order to assign to a courier.
  3. Admin verifies courier availability.
  4. Admin assigns the courier to the order.
  5. System confirms assignment to the courier.
- **Subflows:** None.
- **Alternative Flows:**
  - **Alt 4A:** No available couriers results in a notification to the admin.
- **Assumptions:** Couriers have a live availability status in the system.

### Use Case 12
- **ID:** UC-12
- **Name:** Accept Order Delivery
- **Preconditions:**
  - Courier is assigned an order.
- **Main Flow:**
  1. Courier receives order assignment notification.
  2. Courier views order details.
  3. Courier selects “Accept Order.”
  4. System logs acceptance.
  5. Courier prepares for pick-up at the restaurant.
- **Subflows:** None.
- **Alternative Flows:**
  - **Alt 3A:** Courier declines the order causing re-assignment to another courier.
- **Assumptions:** Courier has necessary equipment and means for delivery.

### Use Case 13
- **ID:** UC-13
- **Name:** Deliver Order
- **Preconditions:**
  - Courier has picked up the order from the restaurant.
- **Main Flow:**
  1. Courier navigates to the customer's address.
  2. Courier verifies order details.
  3. Courier arrives at the delivery location.
  4. Courier hands the order to the customer.
  5. Courier marks the order as delivered in the system.
- **Subflows:** None.
- **Alternative Flows:**
  - **Alt 4A:** Customer is unavailable to receive the order.
- **Assumptions:** Delivery address is accurate.

### Use Case 14
- **ID:** UC-14
- **Name:** Rate and Review Courier
- **Preconditions:**
  - Customer has received their order.
- **Main Flow:**
  1. Customer navigates to the delivery history.
  2. Customer selects the relevant delivery.
  3. Customer rates the courier on a scale (1-5 stars).
  4. Customer provides comments regarding the delivery experience.
  5. Customer submits the review.
- **Subflows:** None.
- **Alternative Flows:**
  - **Alt 3A:** Submission fails if the content is inappropriate.
- **Assumptions:** Customer considered the courier’s service worthy of a rating.

### Use Case 15
- **ID:** UC-15
- **Name:** Admin View Sales Reports
- **Preconditions:**
  - Admin is logged in.
- **Main Flow:**
  1. Admin accesses the analytics section.
  2. Admin selects the time frame for the report.
  3. System generates the sales report.
  4. Admin reviews key metrics (total sales, refunds, etc.).
  5. Admin downloads the report if needed.
- **Subflows:** None.
- **Alternative Flows:**
  - **Alt 4A:** Report generation encounters an error.
- **Assumptions:** Admin has access rights to analytics data.

### Use Case 16
- **ID:** UC-16
- **Name:** Send Notification to Customers
- **Preconditions:**
  - Admin wants to communicate important updates.
- **Main Flow:**
  1. Admin drafts a notification message.
  2. Admin selects the target audience (all users or specific groups).
  3. Admin schedules or sends the notification.
  4. System delivers the notification to customers’ devices.
  5. Customers receive and read the notification.
- **Subflows:** None.
- **Alternative Flows:**
  - **Alt 3A:** Notification fails due to delivery issues.
- **Assumptions:** Customers have enabled notifications on their devices.

### Use Case 17
- **ID:** UC-17
- **Name:** Process Bankcard Payment
- **Preconditions:**
  - Customer has selected a payment method as bankcard.
- **Main Flow:**
  1. System prompts customer for bankcard details.
  2. Customer enters card number, expiration, and CVV.
  3. System validates card details.
  4. System processes the payment.
  5. Customer receives payment confirmation.
- **Subflows:** None.
- **Alternative Flows:**
  - **Alt 4A:** Payment fails due to insufficient funds.
- **Assumptions:** Customer has a valid bankcard.

### Use Case 18
- **ID:** UC-18
- **Name:** Process Cash Payment
- **Preconditions:**
  - Customer has selected cash payment.
- **Main Flow:**
  1. Courier arrives with the order.
  2. Courier requests payment from the customer.
  3. Customer hands over the cash.
  4. Courier confirms receipt of payment.
  5. System marks the order as paid.
- **Subflows:** None.
- **Alternative Flows:**
  - **Alt 3A:** Customer refuses to pay after receiving the order.
- **Assumptions:** Customer has cash available for the payment.

### Use Case 19
- **ID:** UC-19
- **Name:** Admin Manage Restaurant Listings
- **Preconditions:**
  - Admin is logged in.
- **Main Flow:**
  1. Admin accesses the restaurant management section.
  2. Admin views the list of all registered restaurants.
  3. Admin selects an option to add, edit, or remove a restaurant.
  4. Admin completes the action.
  5. System confirms the action and updates the listings.
- **Subflows:** None.
- **Alternative Flows:**
  - **Alt 4A:** Operation fails due to database connection errors.
- **Assumptions:** Admin has sufficient permissions to make changes.

### Use Case 20
- **ID:** UC-20
- **Name:** Add Promo Code
- **Preconditions:**
  - Customer is at checkout.
- **Main Flow:**
  1. Customer selects the option to add a promo code.
  2. Customer enters the promo code into the input field.
  3. System validates the promo code.
  4. System applies the discount to the total order value.
  5. Customer reviews the updated total.
- **Subflows:** None.
- **Alternative Flows:**
  - **Alt 3A:** Invalid promo code results in an error message.
- **Assumptions:** Customer has access to valid promo codes.

### Use Case 21
- **ID:** UC-21
- **Name:** Update Delivery Address
- **Preconditions:**
  - Customer is logged in and has an address in their profile.
- **Main Flow:**
  1. Customer navigates to profile settings.
  2. Customer selects the address section.
  3. Customer edits the delivery address.
  4. Customer submits the changes.
  5. System updates the address in the profile.
- **Subflows:** None.
- **Alternative Flows:**
  - **Alt 4A:** Submission fails due to validation errors.
- **Assumptions:** Customer requires an updated delivery address for future orders.

### Use Case 22
- **ID:** UC-22
- **Name:** View Order History
- **Preconditions:**
  - Customer is logged in.
- **Main Flow:**
  1. Customer navigates to the order history section.
  2. System retrieves past orders.
  3. Customer reviews the list of previous orders.
  4. Customer can select any order to view details.
  5. System displays order details including items and status.
- **Subflows:** None.
- **Alternative Flows:**
  - **Alt 4A:** Order history fails to load due to server issues.
- **Assumptions:** System retains the customer’s order history.

### Use Case 23
- **ID:** UC-23
- **Name:** Receive Customer Feedback
- **Preconditions:**
  - Admin wants to gather user feedback.
- **Main Flow:**
  1. Admin accesses the feedback management section.
  2. Admin views recent feedback entries from customers.
  3. Admin categorizes and evaluates the feedback.
  4. Admin takes action based on feedback if necessary.
  5. System generates a report on user sentiments.
- **Subflows:** None.
- **Alternative Flows:**
  - **Alt 4A:** Feedback fails to load due to network issues.
- **Assumptions:** Admin regularly reviews customer feedback for improvements.

### Use Case 24
- **ID:** UC-24
- **Name:** Set Delivery Time
- **Preconditions:**
  - Customer is placing an order.
- **Main Flow:**
  1. Customer selects items and proceeds to checkout.
  2. Customer chooses the "Schedule Delivery" option.
  3. Customer selects a preferred delivery date and time.
  4. System confirms the selected time slot is available.
  5. Customer submits the scheduled delivery.
- **Subflows:** None.
- **Alternative Flows:**
  - **Alt 4A:** Time slot is unavailable, prompting customer to pick another.
- **Assumptions:** Customers desire flexibility in their delivery timing.

### Use Case 25
- **ID:** UC-25
- **Name:** Share Order with Friends
- **Preconditions:**
  - Customer has placed an order.
- **Main Flow:**
  1. Customer selects the option to share order details.
  2. Customer chooses the sharing method (social media, email, etc.).
  3. Customer confirms sharing the order link.
  4. System generates a sharable link to the order.
  5. Friends receive the link and can view order details.
- **Subflows:** None.
- **Alternative Flows:**
  - **Alt 4A:** Link generation fails, resulting in an error.
- **Assumptions:** Customers want to share their food experiences with others.

### Use Case 26
- **ID:** UC-26
- **Name:** Access Special Offers
- **Preconditions:**
  - Customer is browsing restaurants.
- **Main Flow:**
  1. Customer accesses the "Offers" section in the app.
  2. System displays current special offers available.
  3. Customer selects an offer for details.
  4. Customer adds items to the order utilizing the offer.
  5. System confirms the application of the special offer at checkout.
- **Subflows:** None.
- **Alternative Flows:**
  - **Alt 4A:** Offer has expired, prompting a notification to the customer.
- **Assumptions:** Customers are attracted to promotional deals.

### Use Case 27
- **ID:** UC-27
- **Name:** Issue Refund for Customer Complaint
- **Preconditions:**
  - Customer has raised a complaint.
- **Main Flow:**
  1. Admin reviews the customer complaint.
  2. Admin validates the complaint details and approves a refund.
  3. Admin processes the refund through the payment system.
  4. Customer receives notification of the refund.
  5. System updates the order status to "Refunded."
- **Subflows:** None.
- **Alternative Flows:**
  - **Alt 4A:** Refund process fails due to payment gateway issues.
- **Assumptions:** Admin has the authority to process refunds.

### Use Case 28
- **ID:** UC-28
- **Name:** View App User Manual
- **Preconditions:**
  - Customer or Admin needs assistance with the app.
- **Main Flow:**
  1. User accesses the help section.
  2. User selects "User Manual."
  3. System displays the user manual document.
  4. User navigates through the manual for assistance.
  5. User can download the manual for offline access.
- **Subflows:** None.
- **Alternative Flows:**
  - **Alt 4A:** Manual fails to load due to connectivity issues.
- **Assumptions:** Users seek guidance on app functionalities.

### Use Case 29
- **ID:** UC-29
- **Name:** Change Currency for Payment
- **Preconditions:**
  - Customer is logged in and ready to check out.
- **Main Flow:**
  1. Customer navigates to payment options.
  2. Customer selects the currency dropdown.
  3. System displays available currencies based on location.
  4. Customer selects the desired currency.
  5. System updates the payment total accordingly.
- **Subflows:** None.
- **Alternative Flows:**
  - **Alt 4A:** Currency selection fails due to unsupported currency.
- **Assumptions:** Customers may prefer payments in their local currency.

### Use Case 30
- **ID:** UC-30
- **Name:** Generate User Activity Reports
- **Preconditions:**
  - Admin wants to analyze user activity.
- **Main Flow:**
  1. Admin accesses analytics section.
  2. Admin selects "Generate User Activity Report."
  3. System compiles data for specified time frame.
  4. Admin reviews user engagement and transaction metrics.
  5. Admin downloads the report for further analysis.
- **Subflows:** None.
- **Alternative Flows:**
  - **Alt 4A:** Report generation times out due to server overload.
- **Assumptions:** Admin uses data for improving service efficiency.