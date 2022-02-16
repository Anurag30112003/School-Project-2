from config import mydb , mycursor

def book_room():
    condition = True
    while condition == True:
        login_id = input("Enter your name: ")
        password = input("Enter your password: ")
        mycursor.execute(f"SELECT password FROM customers WHERE name = '{login_id}'")
        result = mycursor.fetchone()
        result = str(result)
        result = result.replace("(","").replace(")","")
        result = result.replace("'","")
        result = result.replace(",","")
        if password == result:
            print("Login Successful")
            mycursor.execute(f"SELECT id FROM customers WHERE name = '{login_id}' ")
            customer_id = mycursor.fetchone()
            print("""
            Enter the type of room you want book: 
            1. VIP
            2. Deluxe
            3.Normal
            """)
            cl = input("Enter your choice: ")
            if cl == '1':
                print("""
                The VIP rooms avilable are:
                """)
                mycursor.execute("SELECT room_number FROM rooms WHERE room_type = 'VIP' AND status = 'empty'")
                myresult = mycursor.fetchall()
                for x in myresult:
                    x = str(x)
                    x = x.replace("(","").replace(")","")
                    x = x.replace("'","")
                    x = x.replace(",","")
                    print("Room Number = ",x)
                room_number = input("Enter the room number you want to book: ")
                mycursor.execute(f"UPDATE rooms SET status = 'booked' , cusname ='{login_id}'  WHERE room_number = '{room_number}' ")
                mycursor.execute(f"UPDATE customers SET rooms = '{room_number}' WHERE name = '{login_id}' ")

                mydb.commit()
                print(f"Room {room_number} booked successfully")
                mydb.commit()
                condition = False
            elif cl == '2':
                print("""
                The Deluxe rooms avilable are:
                """)
                mycursor.execute("SELECT room_number FROM rooms WHERE room_type = 'Deluxe' AND status = 'empty'")
                myresult = mycursor.fetchall()
                for x in myresult:
                    x = str(x)
                    x = x.replace("(","").replace(")","")
                    x = x.replace("'","")
                    x = x.replace(",","")
                    print("Room Number = ",x)
                customerid = ()
                room_number = input("Enter the room number you want to book: ")
                mycursor.execute(f"UPDATE rooms SET status = 'booked' , cusname ='{login_id}'  WHERE room_number = '{room_number}' ")
                mycursor.execute(f"UPDATE customers SET rooms = '{room_number}' WHERE name = '{login_id}' ")
                mydb.commit()
                print(f"Room {room_number} booked successfully")
                condition = False
                    
            elif cl == '3':
                print("""
                The Normal rooms avilable are:
                """)
                mycursor.execute("SELECT room_number FROM rooms WHERE room_type = 'Normal' AND status = 'empty'")
                myresult = mycursor.fetchall()
                for x in myresult:
                    x = str(x)
                    x = x.replace("(","").replace(")","")
                    x = x.replace("'","")
                    x = x.replace(",","")
                    print("Room Number = ",x)
                room_number = input("Enter the room number you want to book: ")
                mycursor.execute(f"UPDATE rooms SET status = 'booked' , cusname ='{login_id}'  WHERE room_number = '{room_number}' ")
                mycursor.execute(f"UPDATE customers SET rooms = '{room_number}' WHERE name = '{login_id}' ")
                mydb.commit()
                print(f"Room {room_number} booked successfully")
                mydb.commit()
                condition = False
            else:
                print("""
                Invalid input.
                """)
        else:
            print("""
            Wrong Passowrd.
            """)
        
    