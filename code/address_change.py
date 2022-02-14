from config import mycursor , mydb

def change_address():
    old_address = input("Enter old address: ")
    new_address = input("Enter new address: ")
    mycursor.execute("UPDATE customers SET address = %s WHERE address = %s", (new_address, old_address))
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")