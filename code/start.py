from table_create import create_table
from columns_add import add_columns
from room_add import add_room
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
        2. Add New room
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
                    3. Exit
                    """)
                    response = input("Enter your choice : ")
                    if response == "1":
                        create_table()
                    elif response == "2":
                        add_columns(table_name=None,response="YES")
                    elif response == "3":
                        print("Thank you !")
                        adminleave = True
                    else:
                        print("Invalid Input !!")
                        start(leave=False)   
        elif response == "2":
            add_room()
        elif response == "3":
            leave = True
        else:
            print("Invalid Input !!")
            start(leave=False)
start(leave)