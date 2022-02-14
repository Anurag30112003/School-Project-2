from customer_add import add_customer
from customer_delete import delete_customer
def customer():
    condition = True
    while condition == True:
        print("""
        What you want to do?
        1. Add a new customer
        2. Delete a customer
        3. Exit
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            add_customer()
        elif choice == "2":
            delete_customer()
        elif choice == "3":
            condition = False
        else:
            print("Invalid choice.")

