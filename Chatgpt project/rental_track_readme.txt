
# Expanded Requirements
# The application allows the user to input essential car rental information:
# - Client information: This includes the client's name, contact number, and company code.
# - Car information: Starting and ending kilometers to track the distance traveled.
# - Rental period: The number of days the car was rented.
# - Discount selection: A dropdown menu to apply discounts (0%, 10%, 20%).
# - Comments: Additional information regarding the rental.
#
# The application calculates and stores the following information:
# - Total kilometers traveled
# - Average kilometers traveled per day
# - Total cost, with discount applied if applicable
# - All this data can be exported to a CSV file for record-keeping.
#
# Expanded How Code Works
# 1. **Tkinter GUI**: The main interface is built using Tkinter.
#    - The user inputs client details, car details, and rental information via text entry fields and a dropdown menu.
# 2. **Calculate Rental Function** (`calculate_rental()`):
#    - Retrieves values from the entry fields.
#    - Validates the data: Ensures `end_km` is greater than `start_km` and `days` is positive.
#    - Displays error indicators (red `*`) next to fields that have incorrect input.
#    - Calculates the total kilometers traveled and average daily kilometers.
#    - Computes the total cost of the rental, applying a discount if selected.
#    - Stores the rental data in a list and displays a success message with the calculated total cost.
# 3. **Export to CSV Function** (`export_to_csv()`):
#    - Converts the rental data into a Pandas DataFrame and saves it as a CSV file.
#    - Displays a confirmation message if the data is successfully exported.
# 4. **Error Handling**:
#    - The `try`-`except` block in `calculate_rental()` ensures that invalid input (e.g., non-numeric values) is caught and prompts the user with an appropriate error message.
#    - Error indicators (red `*`) appear next to incorrect input fields to guide the user.
# 5. **User Experience**:
#    - The program ensures the user cannot proceed with incorrect input by providing clear error messages and requiring correct data entry before proceeding.
# 6. **User Interface Layout**:
#    - The application layout is organized into sections for client information, car details, rental details, comments, and buttons for actions (calculate/save and export).
#    - Labels and entry fields are arranged in a grid layout for simplicity and ease of use.
#    - The window size and aesthetics are improved for better readability and user interaction, with a consistent dark background color and padding.
# 7. **CSV Export**:
#    - The exported CSV file (`automobiliu_nuoma.csv`) contains all the rental details, making it easy for the user to keep records and review past rentals.