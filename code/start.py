from table_create import create_table
from columns_add import add_columns
from customer import customer
from room_add import add_room
from drop_column import cdrop
from databaseshow import showdatabases
from dotenv import load_dotenv
import os
load_dotenv()
adminpass = os.getenv("ADMIN_PASS")
leave = False
# Hotel Manangement system in python with mysql database.
def start(leave):
    while leave == False:
        print("""
        ============================================================
                    Welcome to Hotel Management System.
        ============================================================


        What do you want to do?
        1. Admin Section
        2. Customer Section
        3. Exit
        """)
        response = input("Enter your choice : ")
        if response == "1":
            p = input("Enter your password : ")
            if p == adminpass:
                print("Welcome to Admin Section")
                adminleave = False
                while adminleave == False:
                    print("""
                    What do you want to do?
                    1. Create Table
                    2. Add Columns
                    3. Add Room
                    4. Drop Columns
                    5. Show Tables
                    6. Exit
                    """)
                    response = input("Enter your choice : ")
                    if response == "1":
                        create_table()
                    elif response == "2":
                        add_columns(table_name=None,response="YES")
                    elif response == "3":
                        add_room()
                    elif response == "4":
                        cdrop()
                    elif response == "5":
                        showdatabases()
                    elif response == "6":
                        print("Thank you !")
                        adminleave = True
                    else:
                        print("Invalid Input !!")
                        start(leave=False)   
            else:
                print("Invalid Password !!")
                start(leave=False)
        elif response == "2":
            customer()
        elif response == "3":
            leave = True
        else:
            print("Invalid Input !!")
            start(leave=False)
start(leave)
