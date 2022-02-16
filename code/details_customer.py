from config import mydb,mycursor
def customer_details():
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    mycursor.execute("SELECT phone_number,address,email,rooms FROM customers WHERE name = %s",(name,))
    myresult = mycursor.fetchall()                      
    # print(myresult)
    print(f'''
    Here are your details:
    
    Name: {name}
    Phone Number: {myresult[0][0]}
    Address: {myresult[0][1]}
    Email: {myresult[0][2]}
    Rooms Booked : {myresult[0][3]}


    ''')
    
# customer_details()