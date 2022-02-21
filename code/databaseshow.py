from config import mydb , mycursor

def showdatabases():
    response = input("Enter the table from these (1. Rooms\ 2. Customers) - ")
    if response == '1':
        mycursor.execute('SELECT * FROM rooms')
        b = mycursor.fetchall()
        for i in b:
            print("\n",i)
            print("\n")
            print("="*100)
    elif response == '2':
        mycursor.execute('SELECT * FROM customers')
        b = mycursor.fetchall()
        for i in b:
            print("\n",i)
            print("\n")
            print("="*100)


