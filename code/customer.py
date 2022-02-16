from customer_add import add_customer
from customer_delete import delete_customer
from phonenumber_change import change_phonenumber
from address_change import change_address
from email_change import change_email
from room_book import book_room
from room_leave import leave_room
from details_customer import customer_details
def customer():
    condition = True
    while condition == True:
        print("""
        What you want to do?
        1. Add a new customer
        2. Delete a customer
        3. Change Phonenumber
        4. Change Address
        5. Change Email
        6. Book Room
        7. Leave Room
        8. Customer Details
        9. Exit
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            add_customer()
        elif choice == "2":
            delete_customer()
        elif choice == "3":
            change_phonenumber()
        elif choice == "4":
            change_address()
        elif choice == "5":
            change_email()
        elif choice == "6":
            book_room()
        elif choice == "7":
            leave_room()
        elif choice == "8":
            customer_details()
        elif choice == "9":
            condition = False
        else:
            print("Invalid choice.")

