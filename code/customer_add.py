from config import mydb , mycursor

def add_customer():
    name = input("Enter name: ")
    phone_number = input("Enter phone: ")
    address = input("Enter address: ")
    email = input("Enter email: ")
    sql = "INSERT INTO customers (name, phone_number, address, email) VALUES (%s, %s, %s , %s)" 
    val = (name, phone_number, address, email)
    mycursor.execute(sql, val)
    mydb.commit()
    print(f"Customer {name} added successfully")
