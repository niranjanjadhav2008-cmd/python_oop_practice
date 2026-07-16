from datetime import datetime
import json
class Customer:
    def __init__(self, customer_id, name, email, phone, address):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
    def update_details(self):
        while True:
            print("\nUpdate Customer Details")
            print("1. Name")
            print("2. Email")
            print("3. Phone")
            print("4. Address")
            print("5. Exit")
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            if choice == 1:
                self.name = input("Enter new name: ")
                print("Name updated successfully.")
            elif choice == 2:
                email = input("Enter new email: ")

                if "@" in email and "." in email:
                    self.email = email
                    print("Email updated successfully.")
                else:
                    print("Invalid email address.")
            elif choice == 3:
                phone = input("Enter new phone number: ")
                if phone.isdigit() and len(phone) == 10:
                    self.phone = phone
                    print("Phone number updated successfully.")
                else:
                    print("Invalid phone number.")
            elif choice == 4:
                self.address = input("Enter new address: ")
                print("Address updated successfully.")
            elif choice == 5:
                break
            else:
                print("Invalid choice. Please try again.")
    def display_details(self):
        print("\nCustomer Details")
        print("----------------------------")
        print(f"Customer ID : {self.customer_id}")
        print(f"Name        : {self.name}")
        print(f"Email       : {self.email}")
        print(f"Phone       : {self.phone}")
        print(f"Address     : {self.address}")
class Account:
    def __init__(self, account_number, customer, balance, pin):
        self.account_number = account_number
        self.customer = customer      
        self.balance = balance
        self.pin = pin
    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            self.balance += amount
            print(f"Rs.{amount} deposited successfully.")
            print(f"Current Balance: Rs.{self.balance}")
        else:
            print("Amount must be greater than 0.")
    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Amount must be greater than 0.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Rs.{amount} withdrawn successfully.")
            print(f"Current Balance: Rs.{self.balance}")
    def check_balance(self):
        print(f"Current Balance: Rs.{self.balance}")
    def transfer(self, receiver_account):
        amount = float(input("Enter amount to transfer: "))
        if amount <= 0:
            print("Amount must be greater than 0.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            receiver_account.balance += amount
            print("Money transferred successfully.")
            print(f"Your Balance: Rs.{self.balance}")
    def show_details(self):
        print("\nAccount Details")
        print("----------------------------")
        print(f"Account Number : {self.account_number}")
        print(f"Customer Name  : {self.customer.name}")
        print(f"Balance        : Rs.{self.balance}")
class SavingsAccount(Account):
    def __init__(self, account_number, customer, balance, pin, interest_rate, minimum_balance):
        super().__init__(account_number, customer, balance, pin)
        self.interest_rate = interest_rate
        self.minimum_balance = minimum_balance
    def calculate_interest(self):
        interest = (self.balance * self.interest_rate) / 100
        print(f"Interest Earned: Rs.{interest}")
    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Amount must be greater than 0.")
        elif self.balance - amount < self.minimum_balance:
            print("Withdrawal denied.")
            print(f"You must maintain a minimum balance of Rs.{self.minimum_balance}")
        else:
            self.balance -= amount
            print(f"Rs.{amount} withdrawn successfully.")
            print(f"Current Balance: Rs.{self.balance}")
    def show_details(self):
        super().show_details()
        print(f"Interest Rate  : {self.interest_rate}%")
        print(f"Minimum Balance: Rs.{self.minimum_balance}")
class CurrentAccount(Account):
    def __init__(self, account_number, customer, balance, pin, overdraft_limit):
        super().__init__(account_number, customer, balance, pin)
        self.overdraft_limit = overdraft_limit
    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Amount must be greater than 0.")
        elif amount > self.balance + self.overdraft_limit:
            print("Withdrawal denied.")
            print("Overdraft limit exceeded.")
        else:
            self.balance -= amount
            print(f"Rs.{amount} withdrawn successfully.")
            print(f"Current Balance: Rs.{self.balance}")
    def transfer(self, receiver_account):
        amount = float(input("Enter amount to transfer: "))
        if amount <= 0:
            print("Amount must be greater than 0.")
        elif amount > self.balance + self.overdraft_limit:
            print("Transfer failed.")
            print("Overdraft limit exceeded.")
        else:
            self.balance -= amount
            receiver_account.balance += amount
            print("Money transferred successfully.")
            print(f"Current Balance: Rs.{self.balance}")
    def show_details(self):
        super().show_details()
        print(f"Overdraft Limit : Rs.{self.overdraft_limit}")
class Transaction:
    transaction_count = 1000
    def __init__(self, transaction_type, amount, sender_account, receiver_account=None):
        Transaction.transaction_count += 1
        self.transaction_id = Transaction.transaction_count
        self.transaction_type = transaction_type
        self.amount = amount
        self.sender_account = sender_account
        self.receiver_account = receiver_account
        self.date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    def display_transaction(self):
        print("\nTransaction Details")
        print("----------------------------")
        print(f"Transaction ID : {self.transaction_id}")
        print(f"Type           : {self.transaction_type}")
        print(f"Amount         : Rs.{self.amount}")
        print(f"Date           : {self.date}")
        print(f"Sender Account : {self.sender_account}")
        if self.receiver_account is not None:
            print(f"Receiver Account : {self.receiver_account}")
class Bank:
    def __init__(self):
        self.accounts = []
        self.transactions = []
    def create_account(self, account):
        self.accounts.append(account)
        print("Account created successfully.")
    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None
    def deposit_money(self, account_number):
        account = self.find_account(account_number)
        if account is None:
            print("Account not found.")
            return
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Invalid amount.")
            return
        account.balance += amount
        transaction = Transaction("Deposit", amount, account.account_number)
        self.transactions.append(transaction)
        print("Amount deposited successfully.")
    def withdraw_money(self, account_number):
        account = self.find_account(account_number)
        if account is None:
            print("Account not found.")
            return
        old_balance = account.balance
        account.withdraw()
        if account.balance != old_balance:
            amount = old_balance - account.balance
            transaction = Transaction("Withdraw", amount, account.account_number)
            self.transactions.append(transaction)
    def transfer_money(self, sender_number, receiver_number):
        sender = self.find_account(sender_number)
        receiver = self.find_account(receiver_number)
        if sender is None:
            print("Sender account not found.")
            return
        if receiver is None:
            print("Receiver account not found.")
            return
        old_balance = sender.balance
        sender.transfer(receiver)
        if sender.balance != old_balance:
            amount = old_balance - sender.balance
            transaction = Transaction("Transfer", amount, sender.account_number, receiver.account_number)
            self.transactions.append(transaction)
    def check_balance(self, account_number):
        account = self.find_account(account_number)
        if account is None:
            print("Account not found.")
            return
        account.check_balance()
    def display_account(self, account_number):
        account = self.find_account(account_number)
        if account is None:
            print("Account not found.")
            return
        account.show_details()
    def display_all_accounts(self):
        if len(self.accounts) == 0:
            print("No accounts available.")
            return
        for account in self.accounts:
            account.show_details()
            print("----------------------------")
    def display_transaction_history(self):
        if len(self.transactions) == 0:
            print("No transactions found.")
            return
        for transaction in self.transactions:
            transaction.display_transaction()
            print("----------------------------")
    def delete_account(self, account_number):
        account = self.find_account(account_number)
        if account is None:
            print("Account not found.")
            return
        self.accounts.remove(account)
        print("Account deleted successfully.")

class Database:
    def save_accounts(self, accounts):
        data = []
        for account in accounts:
            account_data = {
                "account_number": account.account_number,
                "customer_id": account.customer.customer_id,
                "name": account.customer.name,
                "email": account.customer.email,
                "phone": account.customer.phone,
                "address": account.customer.address,
                "balance": account.balance,
                "pin": account.pin,
                "account_type": account.__class__.__name__
            }
            if isinstance(account, SavingsAccount):
                account_data["interest_rate"] = account.interest_rate
                account_data["minimum_balance"] = account.minimum_balance
            elif isinstance(account, CurrentAccount):
                account_data["overdraft_limit"] = account.overdraft_limit
            data.append(account_data)
        with open("accounts.json", "w") as file:
            json.dump(data, file, indent=4)
        print("Accounts saved successfully.")
    def load_accounts(self):
        accounts = []
        try:
            with open("accounts.json", "r") as file:
                data = json.load(file)
            for item in data:
                customer = Customer(
                    item["customer_id"],
                    item["name"],
                    item["email"],
                    item["phone"],
                    item["address"]
                )
                if item["account_type"] == "SavingsAccount":
                    account = SavingsAccount(
                        item["account_number"],
                        customer,
                        item["balance"],
                        item["pin"],
                        item["interest_rate"],
                        item["minimum_balance"]
                    )
                else:
                    account = CurrentAccount(
                        item["account_number"],
                        customer,
                        item["balance"],
                        item["pin"],
                        item["overdraft_limit"]
                    )
                accounts.append(account)
        except FileNotFoundError:
            print("No account data found.")
        return accounts
SBI=Bank()
Niranjan=Customer(101,"Niranjan Jadhav","niranjan@gmail.com","9876543210","Pune")
Messi=Customer(102,"Lionel Messi","messi@gmail.com","9876543211","Argentina")
account1=SavingsAccount(121,Niranjan,20000,2008,4,1000)
account2=CurrentAccount(122,Messi,30000,1234,10000)
SBI.create_account(account1)
SBI.create_account(account2)
SBI.display_all_accounts()
SBI.display_account(121)
print(SBI.find_account(121))
SBI.deposit_money(121)
SBI.withdraw_money(122)
SBI.transfer_money(121,122)
SBI.check_balance(121)
SBI.check_balance(122)
SBI.display_transaction_history()
Niranjan.display_details()
Niranjan.update_details()
Niranjan.display_details()
account1.calculate_interest()
SBI.delete_account(122)
SBI.display_all_accounts()
db = Database()
db.save_accounts(SBI.accounts)
loaded_accounts = db.load_accounts()
print(f"Total Accounts Loaded: {len(loaded_accounts)}")
for account in loaded_accounts:
    account.show_details()