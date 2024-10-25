# This is my Banking System project.
Banking System in Python
Overview
This Python application is a simple banking system that allows users to check their account balance, deposit money, and withdraw money using a MySQL database. The system connects to a MySQL database and interacts with user data stored in the user_info table.

Features
Check account balance
Deposit funds
Withdraw funds
Input validation for account existence and fund sufficiency
Requirements
Python 3.x
MySQL Connector for Python
A MySQL database with the name bank
A table named user_info with at least the following columns:
account_no (Primary Key)
balance (Decimal)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/banking-system.git
cd banking-system
Install the required packages:

bash
Copy code
pip install mysql-connector-python
Set up the MySQL database:

Create a database named bank:
sql
Copy code
CREATE DATABASE bank;
Create a user_info table:
sql
Copy code
CREATE TABLE user_info (
    account_no INT PRIMARY KEY,
    balance DECIMAL(10, 2) NOT NULL
);
Insert sample data:
sql
Copy code
INSERT INTO user_info (account_no, balance) VALUES (123456, 1000.00);
Set your database password as an environment variable:

bash
Copy code
export DB_PASSWORD='your_mysql_password'
Usage
Run the application:

bash
Copy code
python banking_system.py
Enter your account number when prompted.

Choose an option from the menu to show balance, deposit, withdraw, or exit.

Code Explanation
Database Connection: The connect_to_db() function establishes a connection to the MySQL database using the provided credentials.
SQL Queries:
sql_query(account_number): Retrieves the current balance for the specified account number.
sql_query_commit(account_number, amount, operation): Updates the balance based on the operation (deposit or withdraw).
if_account_exists(account_number): Checks if the specified account number exists in the database.
User Interactions: The main_system() function manages user input and provides options to the user.
Error Handling
The application handles various input errors and database exceptions to ensure a smooth user experience.
License
This project is licensed under the MIT License.

Contributing
Contributions are welcome! Feel free to submit a pull request or report issues.

Author
Your Name
Acknowledgments
MySQL for the database system
Python for the programming language
