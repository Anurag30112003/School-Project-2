from config import mydb , mycursor

def leave_room():
    room_number = input("Enter room number: ")
    mycursor.execute(f"UPDATE rooms SET status = 'empty' WHERE room_number = '{room_number}' ")
    mydb.commit()
    print(f"Room {room_number} is now empty")