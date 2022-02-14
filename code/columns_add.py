from basic import mycursor, mydb
#Adding columns to the table
def add_columns(response, table_name):
    response = response.upper()
    if response == "Y":
        enter_columns = input("Enter the column name : ")
        mycursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {enter_columns} VARCHAR(255)")
        print(f"Added {enter_columns} successfully")
        # start()
    elif response=="YES" and table_name == None :    
        table_name = input("Enter the table name: ")
        enter_columns = input("Enter the column name : ")
        mycursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {enter_columns} VARCHAR(255)")
        print(f"Added {enter_columns} successfully")
        # start() 
    elif response == "N":
        print("Thank you")
    else:
        print("Invalid Input !!")
        add_columns(response, table_name)
    