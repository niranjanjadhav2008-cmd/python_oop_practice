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
customer1 = Customer(101,"Lionel Messi","messi@gmail.com","9876543210","Rosario, Argentina")
customer1.display_details()
customer1.update_details()
customer1.display_details()