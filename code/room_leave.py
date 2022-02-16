from config import mydb , mycursor

def leave_room():
    login_id = input("Enter your name: ")
    password = input("Enter your password: ")
    mycursor.execute(f"SELECT password FROM customers WHERE name = '{login_id}'")
    result = mycursor.fetchone()
    result = str(result)
    result = result.replace("(","").replace(")","")
    result = result.replace("'","")
    result = result.replace(",","")
    if result == password:
        room_number = input("Enter room number: ")
        mycursor.execute(f"UPDATE rooms SET status = 'empty' WHERE room_number = '{room_number}' ")
        mycursor.execute(f"UPDATE rooms SET cusname = NULL WHERE room_number='{room_number}'")
        mycursor.execute(f"UPDATE customers SET rooms = NULL WHERE name = '{login_id}' ")
        mycursor.execute(f"UPDATE rooms SET booked_on = NULL WHERE room_number = '{room_number}'")
        mydb.commit()
        print(f"Room {room_number} is now empty")