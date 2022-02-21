from config import mydb, mycursor
def delete_customer():
    username = input("Enter name: ")
    mycursor.execute("SELECT name FROM customers WHERE name = %s", (username,))
    customer_name_check = mycursor.fetchone()
    customer_name_check = str(customer_name_check).replace("(", "").replace(")", "").replace(",", "").replace("'", "")
    if customer_name_check == 'None':
        print("Customer does not exist")
    else:
        sql = "DELETE FROM customers WHERE name = %s"
        val = (username,)
        mycursor.execute(sql,val)
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")

