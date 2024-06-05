## GENERAL INFORMATION

**Tester:** Patrick Dyntr

**Preparation and Precondition Notes:**  
Setup your local database with credentials given in README.md file located in folder doc

## ENVIRONMENTAL

**Database engine:** MySQL

**Software and runtime environment:** macOS, phpstorm, Python 3

---

# Test Case: Executability

**Brief description:** Option to start the program  
**Pre-conditions:** Setup your local database with credentials given in README.md file located in folder doc

| Step | Test Steps | Test Data | Expected Result | Notes |
|------|------------|-----------|-----------------|-------|
| 1    | Open VS Code and open terminal in the header of the program | - | A terminal will appear with the current path | |
| 2    | Change the path to your Database_System directory | Command to execute example: `cd /Users/patrick/Downloads/Database_app/src` | Changed path in terminal | Mainly we need to be at directory: `Database_app\src` |
| 3    | Start the main.py file | Command to execute: `python3 main.py` | Connecting to MySQL database...<br>Connection established.<br>Connected to database: ('app1',)<br>Welcome to the e-shop application<br>1. Customers table<br>2. Products table<br>3. Orders table<br>4. Order Items table<br>5. Transactions table<br>6. Generate report<br>7. Import data<br>8. Exit | |

---

# Test Case: CRUD Methods on Tables

**Brief description:** Testing the CRUD methods on tables  
**Pre-conditions:** In README.md file learn what each method is responsible for.

| Step | Test Steps | Test Data | Expected Result | Notes |
|------|------------|-----------|-----------------|-------|
| 1    | Open one of the tables | Enter choice: 1 | --- Customer menu ---<br>1. Create new customer<br>2. Read customer details<br>3. Update customer details<br>4. Delete customer<br>5. Go back<br>Enter choice: | |
| 2    | Create a new customer | Enter choice: 1<br>Enter name: Ondřej Mandík<br>Enter city: Praha<br>Enter credit points: 10000<br>Is customer active (True/False): 0 | Customer created successfully! | |
| 3    | Read customer details | Enter your choice: 2<br>Enter customer ID: 1 | ID: 1<br>Name: Ondřej Mandík<br>City: Praha<br>Credit Points: 10000<br>Is Active: 0 | |
| 4    | Update customer details | Enter your choice: 3<br>Enter customer ID: 1<br>Enter new name: Tomio Okamura<br>Enter new city: Tokyo<br>Enter new credit points: 5000<br>Is customer active (True/False): 1 | Customer updated successfully! | You can check the updated customer by step 2 |
| 5    | Delete customer | Enter your choice: 4<br>Enter customer ID: 1 | Customer deleted successfully | |

---

# Test Case: Generating Summary Report and Importing Data

**Brief description:** How to generate summary report and import data  
**Pre-conditions:** Create a csv file with correspondent data format based on each table attributes. Or use the prepared files in Database_System/data directory

| Step | Test Steps | Test Data | Expected Result | Notes |
|------|------------|-----------|-----------------|-------|
| 1    | In the e-shop main menu generate summary report | Welcome to the e-shop application<br>1. Customers table<br>2. Products table<br>3. Orders table<br>4. Order Items table<br>5. Transactions table<br>6. Generate report<br>7. Import data<br>8. Exit<br>Enter your choice: 6 | -----------------------------<br>Summary Report<br>-----------------------------<br>Customer Data:<br>City, Total Credit Points, Total Customers<br>Praha, 7700.0, 3<br>London, 200.0, 1<br>Paris, 150.0, 1<br>New York, 100.0, 1<br>Product Data:<br>Type, Total Sales<br>Food, 30.0<br>-----------------------------<br>End of Report<br>----------------------------- | This is the example of the tested data. Firstly you need to fill up your data to your tables manually or by importing a csv file to the current table. |
| 2    | In the e-shop main menu Import your business data. | Welcome to the e-shop application<br>1. Customers table<br>2. Products table<br>3. Orders table<br>4. Order Items table<br>5. Transactions table<br>6. Generate report<br>7. Import data<br>8. Exit<br>Enter your choice: 7<br>Enter the file format (csv): csv<br>Enter the file name: product_data.csv<br>Enter the name of the table to import data to: product | Data imported successfully. | Its necessary to have you csv file saved in the \Database_System\doc folder, because the program is reading file from there. |
