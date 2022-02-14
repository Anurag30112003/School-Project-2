from config import mydb, mycursor
def change_phonenumber():
    existing_phonenumber = input("Enter the existing phonenumber: ")
    new_phonenumber = input("Enter the new phonenumber: ")
    mycursor.execute("UPDATE customers SET phone_number = %s WHERE phone_number = %s", (new_phonenumber, existing_phonenumber))
    mydb.commit()
    print(f"Phone number changed successfully to {new_phonenumber}")