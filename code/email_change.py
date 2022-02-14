from config import mydb , mycursor

def change_email():
    old_email = input("Enter your old email: ")
    new_email = input("Enter your new email: ")
    mycursor.execute("UPDATE customers SET email = %s WHERE email = %s", (new_email, old_email))
    mydb.commit()
    print("Email changed successfully")