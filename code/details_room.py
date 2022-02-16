from config import mydb,mycursor
def room_details():
    mycursor.execute("SELECT room_number,room_type,price,status  FROM rooms ")
    result = mycursor.fetchall()
    for i in result:
        print(f'''
        =============================================================
        Room Number = {i[0]}
        Room Type = {i[1]}
        Price = ₹{i[2]}
        Status = {i[3]}
        =============================================================
        ''')
    
# room_details()