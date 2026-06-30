from datetime import datetime
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
