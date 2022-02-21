from config import mydb , mycursor

def check_booking():
    customer_name = input("Enter customer name: ")
    mycursor.execute("SELECT name FROM customers WHERE name = %s", (customer_name,))
    customer_name_check = mycursor.fetchone()
    customer_name_check = str(customer_name_check).replace("(", "").replace(")", "").replace(",", "").replace("'", "")
    if customer_name_check == 'None':
        print("Customer name not found !!")
    else:
        mycursor.execute("SELECT rooms FROM customers WHERE name = %s", (customer_name,))
        rooms = mycursor.fetchone()
        rooms = str(rooms).replace("(", "").replace(")", "").replace(",", "").replace("'", "")
        if rooms == 'None':
            print("No rooms booked.")
        else:
            print("Customer has booked the following rooms:")
            for room in rooms:
                print(room)