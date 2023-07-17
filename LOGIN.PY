def read_balance():
    try:
        with open("BankData.txt", "r") as file:
            balance = float(file.readline())
            return balance
    except FileNotFoundError:
        return 0.0

def write_balance(balance):
    with open("BankData.txt", "w") as file:
        file.write(str(balance))

def write_transaction_log(transaction):
    with open("TransactionLog.txt", "a") as file:
        file.write(transaction + "\n")

def make_transaction():
    while True:
        transaction = input("Would you like to make a transaction? (Yes/No): ").lower()
        if transaction == "yes":
            break
        elif transaction == "no":
            return
        else:
            print("Invalid input. Please enter Yes or No.")

    while True:
        deposit_or_withdrawal = input("Would you like to make a deposit or withdrawal? (Deposit/Withdraw): ").lower()
        if deposit_or_withdrawal == "deposit":
            amount = float(input("How much would you like to deposit? "))
            balance = read_balance()
            balance += amount
            write_balance(balance)
            write_transaction_log(f"Deposit: +{amount}")
            print("Deposit successful.")
            print("Current balance:", balance)
            break
        elif deposit_or_withdrawal == "withdraw":
            amount = float(input("How much would you like to withdraw? "))
            balance = read_balance()
            if amount <= balance:
                balance -= amount
                write_balance(balance)
                write_transaction_log(f"Withdrawal: -{amount}")
                print("Withdrawal successful.")
                print("Current balance:", balance)
                break
            else:
                print("Insufficient funds.")
        else:
            print("Invalid input. Please enter Deposit or Withdraw.")

def display_balance():
    balance = read_balance()
    print("Current balance:", balance)

display_balance()
make_transaction()
