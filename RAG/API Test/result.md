Q1: Generate A Use Case for "New Customer Creates Account"
A1: - ID: UC-01
- Name: New Customer Creates Account
- Preconditions:
  - User has installed the food delivery application on their mobile device.
  - User has a stable internet connection.
  - User has not previously created an account on the application.

- Main Flow:
  1. Open the food delivery application on the mobile device.
  2. Tap on the "Sign Up" or "Create Account" button on the home screen.
  3. Enter a valid email address, and create a password following specified criteria.
  4. Input personal details such as name and phone number.
  5. Agree to the application's terms and conditions and privacy policy.
  6. Submit the registration form to create the account.
  7. Receive an email verification link at the provided email address.
  8. Open the verification email and click on the link to verify the account.
  9. Upon successful verification, log into the application using the registered credentials.

- Subflows:
  - 3.1 If user opts to sign up using social media or third-party services:
    1. Tap on the relevant social media icon.
    2. Grant necessary permissions to share data between the social media account and the food delivery app.
    3. Return to the application, which confirms account creation using the social media credentials.

- Alternative Flows:
  - Step 3: If the user enters an invalid email format, the application prompts the user to re-enter a valid email address.
  - Step 6: If any required field is left blank, the application displays an error message highlighting the missing information.
  - Step 7/8: If the verification email is not received, the user can request a new verification link through the application’s support or account recovery option.

- Assumptions:
  - The application supports account creation through email and social media services.
  - The application has built-in validation for email formats and password criteria.
  - There's a mechanism in place for users to receive and act on email verification.
  - The application is designed to cater to user needs, such as language barriers and accessibility issues, as indicated by previous UX case study mentions.
------------------------------------------------------------
Q2: Generate A Use Case for "Customer Places Order"
A2: - **ID**: UC-01
- **Name**: Customer Places Order
- **Preconditions**:
  - The customer has successfully logged into the food delivery application.
  - The customer has set up a valid payment method within the application.
  - The application displays a list of participating restaurants or food providers with their menus.

- **Main Flow**:
  1. Display the list of available restaurants or food providers to the customer.
  2. Allow the customer to select a restaurant or food provider from the list.
  3. Present the selected restaurant's menu to the customer.
  4. Enable the customer to select one or more items from the menu.
  5. Provide an option for the customer to review their selections in a cart view.
  6. Prompt the customer to enter or verify the delivery address.
  7. Present the total amount including any taxes and delivery fees.
  8. Offer the customer to confirm their order and choose the payment option.
  9. Process the payment using the chosen method.
  10. Display an order confirmation with the estimated delivery time to the customer.

- **Subflows**:
  - **2a. Filter Restaurants**: 
    - From Main Flow Step 1, provide filters such as cuisine type, delivery time, and customer ratings for restaurant selection.
  - **4a. Customize Order**:
    - From Main Flow Step 4, allow customization options for selected items (e.g., ingredients, size options).

- **Alternative Flows**:
  - **3a. Restaurant Not Available**:
    - If the selected restaurant is unavailable (e.g., closed), return to Step 1 with a notification to the customer.
  - **9a. Payment Failure**:
    - If the payment fails, prompt the customer to retry or select a different payment method, returning to Step 8.
  - **10a. Order Modification**:
    - If the customer wishes to modify the order post confirmation but before preparation, enable an option to contact customer support for modifications.

- **Assumptions**:
  - The customer has a stable internet connection for completing the ordering process.
  - The application supports multiple payment options (e.g., credit/debit cards, online banking).
  - The customer’s location is within the serviceable area defined by the application.
  - Restaurants or food service providers are responsible for updating their availability and menu.
------------------------------------------------------------
Q3: Generate A Use Case for "Customer Pays via 3rd-Party Service"
A3: **Use Case for Customer Pays via 3rd-Party Service in Food Delivery Application**

- **ID**: UC-01
- **Name**: Customer Payment via 3rd-Party Service
- **Preconditions**:
  - User must be registered and logged into the app.
  - User has selected items from the food menu and added them to the cart.
  - System has established a connection with the 3rd-party payment service.
  
- **Main Flow**:
  1. Display the list of available payment options to the user.
  2. Prompt the user to select a 3rd-party payment service from the list.
  3. Redirect the user to the selected 3rd-party payment service's platform.
  4. Process the payment on the 3rd-party platform, where the user authorizes the transaction.
  5. Receive transaction confirmation from the 3rd-party service.
  6. Update the order status to "Paid" and notify the user of successful payment.
  7. Complete the checkout process by initiating order preparation and delivery.

- **Subflows**:
  - **3. 3rd-Party Platform Interaction**:
    1. Authenticate the user on the 3rd-party platform, if required.
    2. Display payment details and prompt user for confirmation.

- **Alternative Flows**:
  - **4A. Payment Authorization Failure**:
    1. If the payment fails on the 3rd-party platform, notify the user of the failure.
    2. Return the user to the payment options screen to select a different payment method or retry.
  - **5A. Confirmation Failure**:
    1. If the app does not receive transaction confirmation from the 3rd-party, notify the user of the status.
    2. Suggest the user to contact customer support or retry the payment process.
  
- **Assumptions**:
  - It is assumed that the user is familiar with the chosen 3rd-party payment service.
  - The app can successfully redirect and communicate with various 3rd-party payment services.
  - The availability of 3rd-party payment services varies by location and user preferences.
------------------------------------------------------------
Q4: Generate A Use Case for "Admin Processes Customer Support Request"
A4: - ID: UC-01
- Name: Admin Processes Customer Support Request
- Preconditions:
  - The customer has successfully submitted a support request through the food delivery application.
  - The support request has been logged in the admin support system.
  - An admin is logged into the support management interface.

- Main Flow:
  1. Verify the details of the customer's support request in the system.
  2. Review the order history associated with the support request for background information.
  3. Categorize the request by determining if it is related to delivery, payment, or other issues.
  4. Assign the request to the appropriate customer support specialist team based on the category.
  5. Notify the customer of the support request acknowledgment and the expected response time.
  6. Monitor the status of the support request for timely resolution.

- Subflows:
  - 3a. If the request is related to delivery:
    1. Contact the delivery team for order status clarification.
    2. Review GPS tracking data to verify delivery whereabouts.
  - 3b. If the request is related to payment:
    1. Verify the payment transaction history associated with the order.
    2. Check with the finance department for any payment discrepancies.

- Alternative Flows:
  - 1a. If the system cannot find the support request initially:
    1. Perform an advanced search based on the customer's order ID or email address.
    2. If still not found, escalate to technical support for system verification.
  - 5a. If there is a delay in assigning the request to a support specialist due to high volume:
    1. Send automatic notification to the customer explaining the delay and provide an updated expected response time.

- Assumptions:
  - The details of the support request include identifiable order information to assist in categorization.
  - The admin interface includes functionality for categorizing and assigning support requests.
  - The system has a notification feature to communicate with customers regarding their support requests.
  - There is an established protocol for handling and prioritizing customer support requests across different teams.
------------------------------------------------------------
Q5: Generate A Use Case for "New Resturant Registers Account"
A5: **Use Case for New Restaurant Registers Account**

- **ID**: UC-01
- **Name**: New Restaurant Registers Account on Food Delivery App
- **Preconditions**:
  - The food delivery application is live and operational.
  - The new restaurant has internet connectivity.
  - The restaurant owner has a device capable of accessing the food delivery application (e.g., smartphone or computer).

- **Main Flow**:
  1. Initiate the account registration process by selecting "Register" on the food delivery app's homepage.
  2. Input basic restaurant details such as the restaurant name, address, and contact information in the provided form fields.
  3. Upload necessary documentation proving the legitimacy and compliance of the restaurant (e.g., health certificates).
  4. Create a user account by providing an email and setting a secure password.
  5. Review the entered information and submit the registration form.
  6. Receive a confirmation message indicating the successful submission of the registration request.
  7. Await approval email from the food delivery app administrators, indicating successful account activation.

- **Subflows**:
  - *Step 2 - Detailed Input Process*:
    1. Enter the restaurant's opening hours and delivery preferences.
    2. Provide a brief description of the restaurant's cuisine and potential highlights.
    3. Optional: Select available promotions or marketing plans from the food delivery service's options.

- **Alternative Flows**:
  - *Step 3 - Document Upload Error*:
      1. If the document upload fails, an error message is displayed.
      2. User is prompted to verify the document format and size and try uploading again.
  - *Step 5 - Submission Error*:
      1. If the user submits an incomplete form, an error message details the missing information.
      2. User must correct and complete all required fields before re-submitting.

- **Assumptions**:
  - The detail and documentation requirements conform to regional regulatory standards for food service registration.
  - The food delivery application has an internal verification team to review and approve new restaurant accounts.
  - The application allows for secure handling and storage of sensitive documentation.
------------------------------------------------------------
Q6: Generate A Use Case for "Delivery Driver Registers Account"
A6: - ID: UC-01
- Name: Delivery Driver Registers Account
- Preconditions:
  - The Food Delivery application is installed on the driver's mobile device.
  - The driver has a stable internet connection.
  - The driver possesses necessary documentation for account registration (e.g., driver's license, vehicle registration).

- Main Flow:
  1. Launch the Food Delivery application on the mobile device.
  2. Tap on the "Register" button on the application's home screen.
  3. Enter personal information including name, email address, phone number, and create a password.
  4. Upload mandatory documents such as driver's license and vehicle registration.
  5. Submit the information for verification by tapping the "Submit" button.
  6. Receive a confirmation message that the registration request is under review.
  7. Once verified, the driver receives a notification confirming account activation.
  8. Log in to the application using the registered email and password.

- Subflows:
  - Subflow 3a: If the email address already exists, prompt user to log in or use password recovery.

- Alternative Flows:
  - Alt Flow 4a: If documents upload fails, display an error message with retry option and contact support link.
  - Alt Flow 7a: If verification fails, send a notification detailing reasons for rejection and provide steps for re-submission.

- Assumptions:
  - The snippet does not provide specific UI/UX design guidance, so the registration process is assumed to follow standard mobile application patterns.
  - No details on security protocols are provided, assuming standard encryption methods are used for data privacy.
  - Verification of driver's information is presumed to be semi-automated, potentially involving manual review due to lack of specific back-end process details.
------------------------------------------------------------
Q7: Generate A Use Case for "Customer Cancels Order"
A7: - **ID**: UC-03
- **Name**: Customer Cancels Order
- **Preconditions**:
  - Customer must have an active internet connection.
  - Customer must have a registered account and be logged into the food delivery application.
  - An order must be placed and be in a cancellable status (i.e., the food must not yet be out for delivery).

- **Main Flow**:
  1. Display the user's active orders on the dashboard.
  2. Prompt the user to select the order they wish to cancel.
  3. Present the order details, including the cancel option.
  4. User selects the cancel order function.
  5. Confirm the cancellation action with a pop-up dialog requesting confirmation.
  6. Execute the cancellation upon user confirmation.
  7. Display a cancellation confirmation message to the user.

- **Subflows**:
  - *3a. View Order Details*:
    1. User taps on an order to view more details such as delivery time, restaurant name, and items ordered.
    2. Return control to the main flow for the cancellation process.

- **Alternative Flows**:
  - *5a. User Cancels Confirmation Dialog*:
    1. If the user declines or closes the confirmation dialog, terminate the cancellation process.
    2. Redirect the user back to the order details page.
  - *6a. Order Not Cancellable*:
    1. If the system determines the order is too late to cancel (status is not in a cancellable state), display a message indicating the order cannot be canceled.
    2. Redirect the user back to the list of active orders.
  - *6b. Error During Cancellation*:
    1. If there is a failure at the backend to process the cancellation, display an error message to the user.
    2. Offer the user the option to retry or contact support.

- **Assumptions**:
  - The application supports real-time update of order status, necessary for determining if an order is cancellable.
  - Notifications about immovable order states (e.g., being prepared, out for delivery) are shown to reduce user cancellations ineligible for reimbursement.
  - It is assumed that the cancellation policy allows some window of time for cancellation after placing an order.
------------------------------------------------------------
Q8: Generate A Use Case for "Customer Modifies User Profile"
A8: - ID: UC-02
- Name: Customer Modifies User Profile

- Preconditions:
  - The user is registered in the food delivery application.
  - The user is logged into their account on the food delivery application.
  - The application interface is accessible and functional.

- Main Flow:
  1. Display the user profile screen when the user selects the "Profile" option from the main menu.
  2. Allow the user to edit profile information like name, contact information, and address by selecting the "Edit" button.
  3. Provide input fields for each selectable item, pre-filled with the existing data.
  4. Allow the user to modify the data in the input fields.
  5. Require the user to confirm changes by pressing the "Save" button.
  6. Validate the modified data to ensure it meets format and completeness requirements.
  7. Update the user's profile with the validated data and confirm the changes with a notification.

- Subflows:
  - None

- Alternative Flows:
  - A1: If the user cancels the modification process before finalizing (branch from Step 5):
    1. Discard any changes made to the profile.
    2. Return to the user profile screen without saving changes.
  - A2: If validation fails for any modified data (branch from Step 6):
    1. Highlight the erroneous fields and display an error message.
    2. Prompt the user to correct the errors, and prevent submission without correction.
  - A3: If network connectivity is lost when saving changes (branch from Step 7):
    1. Inform the user of the loss of connectivity with an error message.
    2. Offer the option to retry saving when connectivity is restored.

- Assumptions:
  - The application supports essential accessibility features to cater to varied cognitive abilities, addressing user pain points like language barriers and ease of use.
  - The user's profile fields include only basic information: name, contact information, and address, as no specifics are provided in the context.
  - The application design is user-centered, based on iterative testing and thoughtful research, ensuring a functional editing process.
------------------------------------------------------------
Q9: Generate A Use Case for "User Resets Login Password"
A9: **Use Case: User Resets Login Password**

- **ID**: UC-02
- **Name**: Reset Login Password
- **Preconditions**:
  - The user has a registered account with the Food Delivery application.
  - The user has access to their email associated with the account.
  - The user is unable to log in due to a forgotten password.

- **Main Flow**:
  1. User selects the "Forgot Password?" link on the login screen.
  2. System prompts the user to enter their registered email address.
  3. User inputs their email and selects "Submit."
  4. System verifies the email address and sends a password reset link to it.
  5. User opens the password reset email and clicks on the provided link.
  6. System directs the user to a secure password reset page.
  7. User enters a new password, confirms it, and selects "Reset Password."
  8. System updates the user's password and displays a success message.

- **Alternative Flows**:
  - **A1**: 
    - **From Step 4**: If the system does not recognize the email address, it displays an error message and prompts the user to re-enter the correct email.
  - **A2**:
    - **From Step 5**: If the user does not receive the email:
      - System provides an option to resend the verification email.
  - **A3**:
    - **From Step 7**: If the new password does not meet the security criteria:
      - System prompts the user to re-enter the password following the correct criteria (e.g., minimum length, special characters).

- **Assumptions**:
  - The Food Delivery application requires an email as the primary credential for password reset.
  - Security measures, such as encryption of the reset link and expiration of the link after a tolerance period, are implemented but are outside the scope of this use case.
  - The user has basic internet access to receive and open emails.
------------------------------------------------------------
Q10: Generate A Use Case for "Admin Reviews Delivery Driver(s) Perfomance"
A10: **ID:** UC-01  
**Name:** Admin Reviews Delivery Driver Performance  

**Preconditions:**  
- Admin has access to the Food Delivery Application's admin panel.  
- Delivery driver data, including performance metrics, are available within the system.  
- Admin is authenticated and authorized to review driver performance.  

**Main Flow:**  
1. Log into the admin panel using authorized credentials.  
2. Navigate to the "Driver Performance" section from the dashboard.  
3. Select the specific delivery driver whose performance needs to be reviewed.  
4. View the performance metrics, including delivery times, customer ratings, and number of deliveries.  
5. Analyze the data provided to assess the driver's performance quality.  
6. Record observations and any decisions regarding driver performance, if necessary.  
7. Log out of the admin panel.  

**Subflows:**  
1.1. If login fails, refer to Alternative Flow 1.

**Alternative Flows:**  
1. **Login Failure:**  
   - 1.1. If the admin enters incorrect credentials, display an error message and prompt for re-entry.
   - 1.2. Allow up to three attempts before locking the account temporarily for security purposes.
  
3. **Data Unavailable:**  
   - 3.1. If driver data is not available, display an error message indicating data retrieval issues.
   - 3.2. Provide options to retry loading data or contact technical support.

5. **Metrics Ambiguity:**  
   - 5.1. If metrics are unclear or seem erroneous, provide an option to consult the support team for clarification.

**Assumptions:**  
- The "Driver Performance" section exists within the admin panel, providing essential metrics.
- There is no specific indication of how the performance metrics are calculated or what constitutes a good performance, so it is assumed that qualitative and quantitative metrics are available.
- It is assumed that the admin has the privilege to temporarily lock accounts when login attempts exceed a limit.
------------------------------------------------------------
Q11: Generate A Use Case for "User Reports App issue"
A11: - ID: UC-01
- Name: User Reports App Issue in Food Delivery Application
- Preconditions:
  - User must have an active account in the food delivery application.
  - The application must be installed and logged in on the user's mobile device.
  - The user must experience an issue that disrupts the intended use of the application.
  
- Main Flow:
  1. User encounters an issue while using the food delivery application.
  2. User navigates to the app's support or help section.
  3. User selects the "Report an Issue" option.
  4. User describes the issue in detail using the provided form.
  5. User submits the issue report via the app.
  6. System sends a confirmation to the user that the report has been received.
  7. Support team reviews the submitted issue.
  8. Support team responds to the user with a resolution or further inquiries.

- Subflows:
  - None

- Alternative Flows:
  - 4a. If the user provides insufficient information:
    - The system prompts the user to provide additional details before proceeding to step 5.
  - 5a. If network connectivity is lost:
    - System saves the report locally and attempts to resubmit when connectivity is restored.
  - 8a. If the issue report is not clear:
    - Support team may request more information from the user before proceeding with a resolution.

- Assumptions:
  - The food delivery application has a built-in feature for reporting issues.
  - Users are familiar with the basic navigation of the application to locate the support section.
  - The support team has a structured process for reviewing and responding to issues from users.
------------------------------------------------------------
Q12: Generate A Use Case for "Delivery Driver Views Delivery History"
A12: - ID: UC-01
- Name: Delivery Driver Views Delivery History
- Preconditions:
  - The delivery driver must be logged into the food delivery application.
  - The delivery driver must have completed at least one past delivery.
  - The mobile application must be connected to the internet.

- Main Flow:
  1. Display a dashboard upon the driver's login, including a summary of recent deliveries.
  2. Prompt the driver to access the 'History' section from the main menu.
  3. Retrieve and display the list of previous deliveries, including date, time, location, and order details.
  4. Allow the driver to select a specific delivery entry to view more detailed information, such as customer feedback or earned tips.
  5. Provide options to filter the history by date range, delivery status or earnings.
  6. Enable drivers to export the delivery history data as a CSV file for personal records.

- Subflows:
  - 3a: If no deliveries are found in the history, display a message indicating "No delivery records available".
  
- Alternative Flows:
  - 2a: If the internet connection is lost while retrieving history:
    1. Notify the driver with a "Connection Lost" alert.
    2. Prompt the driver to retry accessing the 'History' section once the connection is restored.
    
  - 4a: If detailed information for a selected entry is unavailable:
    1. Display an error message stating "Detailed information currently unavailable".
    2. Allow the driver to return to the main delivery history list.

- Assumptions:
  - The food delivery application includes a dashboard feature.
  - Internet connectivity is necessary for accessing real-time historical data.
  - Drivers have access to a menu from which history can be accessed.
  - Drivers may want to keep a personal record of their delivery history.
------------------------------------------------------------
Q13: Generate A Use Case for "Delivery Driver Exports Financial Statements"
A13: - ID: UC-07
- Name: Delivery Driver Exports Financial Statements
- Preconditions:
  - The delivery driver is logged into the food delivery application.
  - The delivery driver's account has completed orders with associated financial data.
  - The feature for exporting financial statements is available in the driver section of the application.
- Main Flow:
  1. Navigate to the "Driver Dashboard" screen after logging in.
  2. Select the "Financial Statements" option from the dashboard menu.
  3. Choose the desired time period for the financial statement (e.g., past week, month, or custom dates).
  4. Tap the "Export" button to initiate the export process.
  5. Select the preferred format for the exported document (e.g., PDF, Excel).
  6. Confirm the export action to start generating the statement.
  7. Receive a notification once the financial statement is successfully exported and available for download.
- Alternative Flows:
  - 3a. If the driver selects a custom date range that is invalid (e.g., start date is after the end date):
    1. Display an error message indicating the invalid date range.
    2. Prompt the driver to re-select a valid date range.
  - 5a. If the driver does not have a suitable application to open the selected format:
    1. Display an alert suggesting alternative formats.
    2. Allow the driver to select a different format before confirming the export.
- Assumptions:
  - The app's feature for exporting financial statements is functioning without server issues.
  - The application supports at least common export formats like PDF and Excel.
  - Notification settings are enabled for the driver to receive alerts about the export process status.
------------------------------------------------------------
Q14: Generate A Use Case for "Customer Links Social Media Account for Login"
A14: - **ID**: UC-01  
- **Name**: Customer Links Social Media Account for Login  

- **Preconditions**:
  - User has a registered social media account.
  - User has the Food Delivery application installed on their device.

- **Main Flow**:
  1. Open the Food Delivery application on your device.
  2. Navigate to the login screen of the application.
  3. Select the option to log in using a social media account.
  4. Choose the desired social media platform from the list provided.
  5. Authorize the Food Delivery application to access the user’s social media account credentials.
  6. Complete the login process and gain access to the Food Delivery application using the linked social media account.

- **Subflows**:
  - **Subflow 1**: If the user is already logged into their social media account on the device, automatically forward them to the authorization step (Step 5).

- **Alternative Flows**:
  - **Alt Flow 1**: If the user does not have the social media app installed on their device, prompt them to install the app or opt for a different login method (after Step 4).
  - **Alt Flow 2**: If the user does not authorize the Food Delivery application, display a cancellation message and provide an option to return to the login screen (after Step 5).
  - **Alt Flow 3**: If the social media account linking fails due to connectivity issues, show an error message and suggest trying again later (after Step 5).

- **Assumptions**:
  - The Food Delivery application supports multiple social media platforms for login.
  - The user is comfortable using social media accounts for logging into third-party applications.
------------------------------------------------------------
Q15: Generate A Use Case for "Resturant Submits Complaint on Delivery Driver"
A15: ### Use Case

- **ID:** UC-03
- **Name:** Restaurant Submits Complaint on Delivery Driver
- **Preconditions:**
  - The restaurant is registered on the food delivery platform.
  - The delivery driver is associated with the platform.
  - The delivery in question has been completed.
  - The restaurant access to the complaint submission feature on the platform.

- **Main Flow:**
  1. Restaurant logs into the food delivery application.
  2. Restaurant navigates to the “Order History” section.
  3. Restaurant selects the specific order related to the complaint.
  4. Restaurant clicks on the “Submit Complaint” button.
  5. System displays a form for complaint submission.
  6. Restaurant fills out details of the complaint, including any necessary driver, order details, or specific incident observations.
  7. Restaurant submits the complaint form.
  8. System confirms receipt of the complaint and notifies the appropriate internal team for review.

- **Subflows:**
  - **6a.** If the restaurant wants to attach images or further documentation:
    1. Restaurant clicks on the “Attach Files” option.
    2. System prompts the restaurant to upload files from device storage.
    3. Restaurant selects and uploads the desired files.
    4. System confirms the successful upload of files.

- **Alternative Flows:**
  - **5a. Unable to Access Complaint Form:**
    1. If the system fails to load the complaint form, the system displays an error message.
    2. Restaurant retries accessing the form by refreshing the page or contacts customer support for assistance.
    
  - **7a. Submission Error:**
    1. If there's an error during the submission of the complaint, an error message is displayed.
    2. Restaurant checks the form for errors or missing information and attempts to submit again.
    
  - **8a. Notification Failure:**
    1. If the system fails to send a confirmation notification, it logs the issue and re-attempts to send it at a later time.

- **Assumptions:**
  - The food delivery application includes a designated complaint mechanism for restaurant users.
  - The application infrastructure supports file uploads for additional complaint documentation.
  - There are designated internal teams responsible for reviewing and acting on submitted complaints.
------------------------------------------------------------
