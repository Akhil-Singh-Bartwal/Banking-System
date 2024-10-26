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
2. Install the required packages:
   ```bash
   pip install mysql-connector-python
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
- Insert some sample data into the `user_info` table:
  ```sql
  INSERT INTO user_info (account_no, balance) VALUES (123456, 1000.00);
- Set the database password:
  ```bash
  export DB_PASSWORD='your_mysql_password'
- (On Windows, use `set` instead of `export`.)

## Usage
Run the application using:
  ```bash
  python <script-name>.py
  ```
Follow the prompts to enter your account number and select the desired banking operation.
