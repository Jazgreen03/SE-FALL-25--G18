 ### Use Case 1
- **ID:** UC-01
- **Name:** User Registration
- **Preconditions:**
  - User has the food delivery app installed.
  - User has a valid email address or phone number.
- **Main Flow:**
  1. Open the app.
  2. Click on "Sign Up."
  3. Enter email/phone number and password.
  4. Provide necessary personal information (name, delivery address).
  5. Click on "Submit."
  6. Receive a verification email or code.
  7. Verify account via email or code.
- **Subflows:** None
- **Alternative Flows:**
  - **Alt 6A:** User does not receive verification email/code.
- **Assumptions:** None

### Use Case 2
- **ID:** UC-02
- **Name:** User Login
- **Preconditions:**
  - User is registered and has account details.
- **Main Flow:**
  1. Open the app.
  2. Click on "Login."
  3. Enter registered email/phone number and password.
  4. Click on "Log In."
  5. Access user dashboard.
- **Subflows:** None
- **Alternative Flows:**
  - **Alt 3A:** User enters incorrect credentials.
  - **Alt 4A:** User forgot password.
- **Assumptions:** None

### Use Case 3
- **ID:** UC-03
- **Name:** Browse Restaurants
- **Preconditions:**
  - User is logged into their account.
- **Main Flow:**
  1. Navigate to "Browse Restaurants."
  2. Filter restaurants by cuisine or rating.
  3. Scroll through the list of restaurants.
  4. Click on a restaurant to view the menu.
- **Subflows:** None
- **Alternative Flows:**
  - **Alt 2A:** No restaurants available for selected filters.
- **Assumptions:** None

### Use Case 4
- **ID:** UC-04
- **Name:** Place an Order
- **Preconditions:**
  - User has browsed through available restaurants.
- **Main Flow:**
  1. Select a restaurant.
  2. Choose items from the menu.
  3. Add items to the cart.
  4. Review cart and make adjustments if needed.
  5. Click on "Proceed to Checkout."
  6. Enter delivery address if not previously saved.
  7. Confirm order and make payment.
- **Subflows:**
  - **Subflow 6A:** Entering a new delivery address.
- **Alternative Flows:**
  - **Alt 7A:** Payment fails.
- **Assumptions:** None

### Use Case 5
- **ID:** UC-05
- **Name:** Track Order Status
- **Preconditions:**
  - User has placed an order.
- **Main Flow:**
  1. Open the app.
  2. Navigate to "My Orders."
  3. Select the active order.
  4. View real-time tracking information.
- **Subflows:** None
- **Alternative Flows:**
  - **Alt 3A:** Delivery status not updating.
- **Assumptions:** None

### Use Case 6
- **ID:** UC-06
- **Name:** Rate and Review Restaurant
- **Preconditions:**
  - User has completed an order from a restaurant.
- **Main Flow:**
  1. Navigate to "My Orders."
  2. Select completed order.
  3. Click on "Rate Restaurant."
  4. Provide a star rating and review comments.
  5. Submit rating and review.
- **Subflows:** None
- **Alternative Flows:**
  - **Alt 4A:** User submits a blank review.
- **Assumptions:** None

### Use Case 7
- **ID:** UC-07
- **Name:** Retrieve Lost Password
- **Preconditions:**
  - User has forgotten their password.
- **Main Flow:**
  1. Open the app.
  2. Click on "Forgot Password?"
  3. Enter registered email/phone number.
  4. Receive password reset instructions.
  5. Follow instructions to reset the password.
- **Subflows:** None
- **Alternative Flows:**
  - **Alt 4A:** User does not receive reset instructions.
- **Assumptions:** None

### Use Case 8
- **ID:** UC-08
- **Name:** Add Payment Method
- **Preconditions:**
  - User is logged in.
- **Main Flow:**
  1. Navigate to "Payment Methods."
  2. Click on "Add Payment Method."
  3. Enter payment information (card number, expiration date, CVC).
  4. Save payment details.
  5. Confirm payment method is added successfully.
- **Subflows:** None
- **Alternative Flows:**
  - **Alt 3A:** Input error in payment information.
- **Assumptions:** None

### Use Case 9
- **ID:** UC-09
- **Name:** Remove Payment Method
- **Preconditions:**
  - User has at least one saved payment method.
- **Main Flow:**
  1. Navigate to "Payment Methods."
  2. Select a payment method to remove.
  3. Click on "Remove."
  4. Confirm removal of payment method.
- **Subflows:** None
- **Alternative Flows:**
  - **Alt 3A:** User attempts to remove the only payment method.
- **Assumptions:** None

### Use Case 10
- **ID:** UC-10
- **Name:** Assign Delivery to Courier
- **Preconditions:**
  - Admin is logged into the management panel.
- **Main Flow:**
  1. Navigate to "Orders Awaiting Delivery."
  2. Select an order for delivery.
  3. Click on "Assign to Courier."
  4. Choose available courier from the list.
  5. Confirm assignment to courier.
- **Subflows:** None
- **Alternative Flows:**
  - **Alt 4A:** No couriers available for assignment.
- **Assumptions:** None

### Use Case 11
- **ID:** UC-11
- **Name:** Update Delivery Status
- **Preconditions:**
  - Courier is logged in and has a delivery assigned.
- **Main Flow:**
  1. Open the app and navigate to "Deliveries."
  2. Select the active delivery.
  3. Click on "Update Status."
  4. Choose status (e.g., preparing, on the way, delivered).
  5. Confirm status update.
- **Subflows:** None
- **Alternative Flows:**
  - **Alt 4A:** Status update fails due to network issues.
- **Assumptions:** None

### Use Case 12
- **ID:** UC-12
- **Name:** Cancel Order
- **Preconditions:**
  - User has placed an order.
- **Main Flow:**
  1. Navigate to "My Orders."
  2. Select the order to be canceled.
  3. Click on "Cancel Order."
  4. Confirm the cancellation.
  5. Receive confirmation of the order cancellation.
- **Subflows:** None
- **Alternative Flows:**
  - **Alt 4A:** User attempts to cancel after a certain time limit.
- **Assumptions:** None

### Use Case 13
- **ID:** UC-13
- **Name:** Contact Support
- **Preconditions:**
  - User is logged in.
- **Main Flow:**
  1. Navigate to "Help & Support."
  2. Click on "Contact Support."
  3. Choose a contact method (chat, email, phone).
  4. Provide details of the issue.
  5. Submit the request for support.
- **Subflows:** None
- **Alternative Flows:**
  - **Alt 4A:** Support request submission fails.
- **Assumptions:** None

### Use Case 14
- **ID:** UC-14
- **Name:** Update Personal Information
- **Preconditions:**
  - User is logged in.
- **Main Flow:**
  1. Navigate to "Profile Settings."
  2. Click on "Edit Profile."
  3. Update personal information (name, address, phone number).
  4. Save changes.
  5. Confirm success message.
- **Subflows:** None
- **Alternative Flows:**
  - **Alt 3A:** User inputs invalid address format.
- **Assumptions:** None

### Use Case 15
- **ID:** UC-15
- **Name:** Restaurant Registration
- **Preconditions:**
  - Restaurant owner has a valid business license.
- **Main Flow:**
  1. Open the app and select "Restaurant Registration."
  2. Fill out the registration form with business details.
  3. Upload necessary documents (license, menu).
  4. Submit the registration form.
  5. Receive confirmation of registration.
- **Subflows:** None
- **Alternative Flows:**
  - **Alt 3A:** Missing documents during submission.
- **Assumptions:** None

### Use Case 16
- **ID:** UC-16
- **Name:** Update Restaurant Menu
- **Preconditions:**
  - Restaurant owner is logged in.
- **Main Flow:**
  1. Navigate to "Menu Management."
  2. Select items to update/add/remove.
  3. Edit necessary details (price, description).
  4. Save changes.
  5. Confirm updates have been made.
- **Subflows:** None
- **Alternative Flows:**
  - **Alt 3A:** Unable to save due to server error.
- **Assumptions:** None

### Use Case 17
- **ID:** UC-17
- **Name:** View Delivery History
- **Preconditions:**
  - User is logged in.
- **Main Flow:**
  1. Navigate to "Order History."
  2. Select "Delivery History."
  3. Browse through past orders.
  4. Click on any order for more details.
- **Subflows:** None
- **Alternative Flows:**
  - **Alt 2A:** No delivery history available.
- **Assumptions:** None

### Use Case 18
- **ID:** UC-18
- **Name:** Set Favorite Restaurants
- **Preconditions:**
  - User is logged in.
- **Main Flow:**
  1. Browse through the list of restaurants.
  2. Click on a restaurant to view details.
  3. Click on "Add to Favorites."
  4. Confirm that the restaurant has been added.
- **Subflows:** None
- **Alternative Flows:**
  - **Alt 3A:** Restaurant already in favorites list.
- **Assumptions:** None

### Use Case 19
- **ID:** UC-19
- **Name:** View Restaurant Ratings
- **Preconditions:**
  - User is browsing restaurants.
- **Main Flow:**
  1. Select a restaurant from the list.
  2. Scroll to the ratings section.
  3. View average star rating and user reviews.
- **Subflows:** None
- **Alternative Flows:**
  - **Alt 2A:** No ratings available for the restaurant.
- **Assumptions:** None

### Use Case 20
- **ID:** UC-20
- **Name:** Receive Promotional Offers
- **Preconditions:**
  - User has opted into notifications.
- **Main Flow:**
  1. Open the app and go to "Promotions."
  2. Browse available promotional offers.
  3. Click on an offer to view details.
  4. Apply the offer when ordering.
- **Subflows:** None
- **Alternative Flows:**
  - **Alt 3A:** Offer not applicable to selected items.
- **Assumptions:** None

### Use Case 21
- **ID:** UC-21
- **Name:** Evaluate Courier Performance
- **Preconditions:**
  - Admin is logged into the management panel.
- **Main Flow:**
  1. Navigate to "Courier Performance."
  2. Select a courier from the list.
  3. View performance metrics (delivery time, ratings).
  4. Generate reports based on these metrics.
- **Subflows:** None
- **Alternative Flows:**
  - **Alt 2A:** No performance data available.
- **Assumptions:** None

### Use Case 22
- **ID:** UC-22
- **Name:** Respond to Customer Feedback
- **Preconditions:**
  - Admin has accessed feedback.
- **Main Flow:**
  1. Navigate to "Customer Feedback."
  2. Select a feedback entry to respond to.
  3. Click on "Respond."
  4. Write a response.
  5. Submit the response.
- **Subflows:** None
- **Alternative Flows:**
  - **Alt 4A:** Response submission fails.
- **Assumptions:** None

### Use Case 23
- **ID:** UC-23
- **Name:** Manage Admin Users
- **Preconditions:**
  - Admin has appropriate permissions.
- **Main Flow:**
  1. Navigate to "User Management."
  2. Click on "Add Admin User."
  3. Enter new user details and permissions.
  4. Save the new admin user.
  5. Confirm the admin user has been added.
- **Subflows:** None
- **Alternative Flows:**
  - **Alt 2A:** Duplicate admin user attempt.
- **Assumptions:** None

### Use Case 24
- **ID:** UC-24
- **Name:** Update App Version
- **Preconditions:**
  - Admin is logged into the management panel.
- **Main Flow:**
  1. Navigate to "App Management."
  2. Click on "Update Version."
  3. Upload the new version details.
  4. Schedule or initiate the update.
  5. Confirm successful update.
- **Subflows:** None
- **Alternative Flows:**
  - **Alt 4A:** Update fails due to compatibility issues.
- **Assumptions:** None

### Use Case 25
- **ID:** UC-25
- **Name:** Filter Order History
- **Preconditions:**
  - User is logged in.
- **Main Flow:**
  1. Navigate to "Order History."
  2. Click on "Filter Orders."
  3. Select filtering criteria (date, restaurant).
  4. Apply filters.
  5. View filtered results.
- **Subflows:** None
- **Alternative Flows:**
  - **Alt 4A:** No orders match the selected filters.
- **Assumptions:** None

### Use Case 26
- **ID:** UC-26
- **Name:** Redeem Loyalty Points
- **Preconditions:**
  - User has accrued loyalty points.
- **Main Flow:**
  1. Open the app and navigate to "Loyalty Points."
  2. Check available points.
  3. Select an option to redeem points.
  4. Confirm point redemption.
  5. Receive confirmation of redemption.
- **Subflows:** None
- **Alternative Flows:**
  - **Alt 4A:** Insufficient points for redemption.
- **Assumptions:** None

### Use Case 27
- **ID:** UC-27
- **Name:** Send Promotional Notifications
- **Preconditions:**
  - Admin is logged in.
- **Main Flow:**
  1. Navigate to "Promotions Management."
  2. Click on "Create New Promotion."
  3. Fill in promotion details (discount, expiry).
  4. Choose target audience.
  5. Send notifications to users.
- **Subflows:** None
- **Alternative Flows:**
  - **Alt 3A:** Invalid promotion details entered.
- **Assumptions:** None

### Use Case 28
- **ID:** UC-28
- **Name:** View Analytics Dashboard
- **Preconditions:**
  - Admin is logged in.
- **Main Flow:**
  1. Navigate to "Analytics Dashboard."
  2. Review key metrics (sales, user engagement).
  3. Explore reports using different views (daily, weekly).
  4. Download detailed reports if needed.
- **Subflows:** None
- **Alternative Flows:**
  - **Alt 3A:** Metrics not available for the selected period.
- **Assumptions:** None

### Use Case 29
- **ID:** UC-29
- **Name:** Sign Out
- **Preconditions:**
  - User is logged in.
- **Main Flow:**
  1. Open the app.
  2. Navigate to "Account Settings."
  3. Click on "Sign Out."
  4. Confirm sign-out action.
- **Subflows:** None
- **Alternative Flows:**
  - **Alt 3A:** User cancels the sign-out action.
- **Assumptions:** None

### Use Case 30
- **ID:** UC-30
- **Name:** Report a Problem with the App
- **Preconditions:**
  - User is logged in.
- **Main Flow:**
  1. Navigate to "Help & Support."
  2. Click on "Report a Problem."
  3. Describe the issue in the provided form.
  4. Submit the report.
  5. Receive confirmation of the report submission.
- **Subflows:** None
- **Alternative Flows:**
  - **Alt 4A:** Report submission fails.
- **Assumptions:** None