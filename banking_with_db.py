import os
import sys
import mysql.connector


def connect_to_db():
    # os.environ['DB_PASSWORD'] = 'Akhil@mysql' # only for vscode
    password = os.environ.get("DB_PASSWORD")
    connect = mysql.connector.connect(
        database="bank", host="localhost", user="root", passwd=password
    )

    return connect


def sql_query(account_number: int) -> int:
    cursor = connect.cursor()
    query = "SELECT balance FROM user_info WHERE account_no = %s"
    cursor.execute(query, (account_number,))
    data = cursor.fetchone()
    cursor.close()
    return data[0]


def sql_query_commit(account_number: int, amount: int, operation: str):
    cursor = connect.cursor()
    query = "UPDATE user_info SET balance = balance + %s WHERE account_no = %s"
    if operation == "withdraw":
        amount = -amount
    cursor.execute(
        query,
        (
            amount,
            account_number,
        ),
    )
    connect.commit()
    cursor.close()


def if_account_exists(account_number: int):
    cursor = connect.cursor()
    query = "SELECT EXISTS( SELECT 1 FROM user_info WHERE account_no = %s)"
    cursor.execute(query, (account_number,))
    exists = cursor.fetchone()[0]
    cursor.close()
    if not exists:
        print("Account does not exists.")
        connect.close()
        sys.exit()


def show_balance(account_number: int):
    current_balance: int = sql_query(account_number)
    print("************************")
    print(f"Your balance is: ₹{current_balance:.2f}")
    print("************************")


def deposit_amount(account_number: int):
    print("************************")
    add_amount: int = int(input("Enter the amount you want to deposit: "))
    print("************************")
    if add_amount > 0:
        operation: str = "deposit"
        sql_query_commit(account_number, add_amount, operation)
    else:
        raise ValueError


def withdraw_amount(account_number: int):
    cursor = connect.cursor()
    query = "SELECT balance FROM user_info WHERE account_no = %s"
    cursor.execute(query, (account_number,))
    current_balance: int = cursor.fetchone()[0]
    operation: str = "withdraw"
    print("************************")
    sub_amount: int = int(input("Enter the amount you want to withdraw: "))
    print("************************")
    if sub_amount == 0:
        raise ValueError
    elif sub_amount <= current_balance:
        sql_query_commit(account_number, sub_amount, operation)
    else:
        print("************************")
        print("  !Insufficient Funds!  ")
        print("************************")


connect = connect_to_db()


def main_system():
    try:
        account_number: int = int(input("Enter you account number: "))
        if_account_exists(account_number)
        while True:
            print("************************")
            print("     Banking System     ")
            print("************************")
            print("1. Show Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            print("************************")

            choice: int = int(input("Enter your choice (1-4): "))
            if choice == 1:
                show_balance(account_number)
            elif choice == 2:
                deposit_amount(account_number)
            elif choice == 3:
                withdraw_amount(account_number)
            elif choice == 4:
                break

    except (ValueError, TypeError):
        print("************************")
        print("    !Invalid input!     ")
        print("************************")
    finally:
        connect.close()


if __name__ == "__main__":
    main_system()
