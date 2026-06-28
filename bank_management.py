class Customer:
    def __init__(self,customer_id,name,email,phone,address):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
    def update_details(self):
        print("Choose corresponding number to update the detail: ")
        print("1 . Customer id")
        print("2 . Name")
        print("3 . Email")
        print("4 . Phone")
        print("5 . Address")
        print("6 . Exit")
        update_details_number = 0
        while True:
            update_details_number = int(input("Enter a number: "))
            if update_details_number == 1:
                self.customer_id = input("Enter your new Customer id: ")
                print(f"Your Customer id updated to {self.customer_id}")
                break
            elif update_details_number == 2:
                self.name = input("Enter Your new Name: ")
                print(f"Your Name updated to {self.name}")
                break
            elif update_details_number == 3:
                self.email = input("Enter Your new Email: ")
                print(f"Your Email updated to {self.email}")
                break
            elif update_details_number == 4:
                self.phone = input("Enter Your new Phone number: ")
                print(f"Your Phone number updated to {self.phone}")
                break
            elif update_details_number == 5:
                self.address = input("Enter your new Address: ")
                print(f"Your Address updated to {self.address}")
                break
            elif update_details_number == 6:
                break
            else:
                print("Enter a valid number")
    def display_details(self):
        print("Customer")
        print("--------------------")
        print(f"ID : {self.customer_id}")
        print(f"Name : {self.name}")
        print(f"Email : {self.email}")
        print(f"Phone : {self.phone}")
c1 = Customer(101,"messi","ajfn",9583920488,"wfnjefenf")
c1.update_details()
c1.display_details()