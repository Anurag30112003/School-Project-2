from config import mydb , mycursor

def book_room():
    condition = True
    while condition == True:
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
            mycursor.execute("SELECT room_number FROM rooms WHERE room_type = 'VIP'")
            myresult = mycursor.fetchall()
            for x in myresult:
                x = str(x)
                x = x.replace("(","").replace(")","")
                x = x.replace("'","")
                x = x.replace(",","")
                print("Room Number = ",x)
            condition = False
        elif cl == '2':
            print("""
            The Deluxe rooms avilable are:
            """)
            mycursor.execute("SELECT room_number FROM rooms WHERE room_type = 'Deluxe'")
            myresult = mycursor.fetchall()
            for x in myresult:
                x = str(x)
                x = x.replace("(","").replace(")","")
                x = x.replace("'","")
                x = x.replace(",","")
                print("Room Number = ",x)
            condition = False
                
        elif cl == '3':
            print("""
            The Normal rooms avilable are:
            """)
            mycursor.execute("SELECT room_number FROM rooms WHERE room_type = 'Normal'")
            myresult = mycursor.fetchall()
            for x in myresult:
                x = str(x)
                x = x.replace("(","").replace(")","")
                x = x.replace("'","")
                x = x.replace(",","")
                print("Room Number = ",x)
            condition = False
        else:
            print("""
            Invalid input.
            """)
    