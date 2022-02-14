from table_create import create_table
from columns_add import add_columns
leave = False
# Hotel Manangement system in python with mysql database.
def start(leave):
    while leave == False:
        print("""
        What do you want to do?
        1. Create Table
        2. Add Columns
        3. Exit
        """)
        response = input("Enter your choice : ")
        if response == "1":
            create_table()
        elif response == "2":
            add_columns(table_name=None,response="YES")
        elif response == "3":
            print("Thank you !")
            leave = True
        else:
            print("Invalid Input !!")
            start(leave=False)   
start(leave)
        