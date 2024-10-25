# This is my Banking System project.
# Banking System in Python

## Overview
This Python application is a simple banking system that allows users to check their account balance, deposit money, and withdraw money using a MySQL database. The system connects to a MySQL database and interacts with user data stored in the `user_info` table.

## Features
- Check account balance
- Deposit funds
- Withdraw funds
- Input validation for account existence and fund sufficiency

## Requirements
- Python 3.x
- MySQL Connector for Python
- A MySQL database with the name `bank`
- A table named `user_info` with at least the following columns:
  - `account_no` (Primary Key)
  - `balance` (Decimal)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/banking-system.git
   cd banking-system
