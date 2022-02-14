from config import mydb, mycursor
def delete_customer():
    username = input("Enter name: ")
    sql = "DELETE FROM customers WHERE name = %s"
    val = (username,)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")

