# Banking System in Python

## Overview
This Python application is a simple banking system that allows users to check their account balance, deposit money, and withdraw money using a MySQL database. The system connects to a MySQL database and interacts with user data stored in the `user_info` table.

## Features
- Check account balance
- Deposit funds
- Withdraw funds
- Input validation for account existence and fund sufficiency

## Requirements
- Python 3.12
- MySQL Connector for Python
- A MySQL database with the name `bank`
- A table named `user_info` with at least the following columns:
  - `account_no` (Primary Key)
  - `balance` (Decimal)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/akhil-singh-bartwal/banking-system.git
   cd banking-system
   ```
2. Install the required packages:
   ```bash
   pip install mysql-connector-python
   ```
3. Set up the MySQL database:
- Ensure MySQL is installed and running.
- Create a database named `bank` and a table named `user_info`:
  ```sql
  CREATE DATABASE bank;
  USE bank;
  CREATE TABLE user_info (
    account_no INT PRIMARY KEY,
    balance FLOAT
  );
  ```
- Insert some sample data into the `user_info` table:
  ```sql
  INSERT INTO user_info (account_no, balance) VALUES (123456, 1000.00);
  ```
- Set the database password:
  ```bash
  export DB_PASSWORD='your_mysql_password'
  ```
- (On Windows, use `set` instead of `export`.)

## Usage
Run the application using:
  ```bash
  python <script-name>.py
  ```
Follow the prompts to enter your account number and select the desired banking operation.

## Code Structure
- `connect_to_db`: Establishes a connection to the MySQL database.
- `sql_query`: Retrieves the current balance of a given account number.
- `sql_query_commit`: Updates the account balance based on the operation (deposit/withdraw).
- `if_account_exists`: Checks if the account number exists in the database.
- `show_balance`: Displays the current balance of the user.
- `deposit_amount`: Prompts the user to deposit an amount and updates the balance.
- `withdraw_amount`: Prompts the user to withdraw an amount, checks for sufficient funds, and updates the balance.
- `main_system`: Main loop that drives the banking operations.

## Error Handling
The application includes basic error handling for invalid inputs and attempts to withdraw more than the current balance.

## License
This project is licensed under the MIT License.

## Contributing
Feel free to submit issues and pull requests if you have suggestions or improvements.
```bash
Make sure to replace `<repository-url>` and `<script-name>` with your actual repository URL and the name of your script before posting.
```
