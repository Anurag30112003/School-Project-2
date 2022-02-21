from config import mydb , mycursor

def add_customer():
        name = input("Enter name: ")
        while True:
            phone_number = input("Enter phone: ")
            if len(phone_number) == 10:
                break
            else:
                print("Please enter a valid phone number")       
        while True:
            email = input("Enter Email: ")
            if '@' in email:
                address = input("Enter address: ")
                password = input("Make password: ")
                sql = "INSERT INTO customers (name, phone_number, address, email,password) VALUES (%s, %s, %s , %s,%s)" 
                val = (name, phone_number, address, email,password)
                mycursor.execute(sql, val)
                mydb.commit()
                print(f"Customer {name} added successfully")
                break
            else:
                print("Invalid email")