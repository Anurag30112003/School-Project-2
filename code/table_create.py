import mysql.connector
import os
from dotenv import load_dotenv
from columns_add import add_columns
load_dotenv()

password = os.getenv("PASSWORD")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=f'{password}',
    database="hotel_management"
)
mycursor = mydb.cursor()
# Creating a new table.
def create_table():
    table_name = input("Enter the table name: ")
    enter_columns = input("Enter the columns: ")
    print("")
    new_table = f"CREATE TABLE hotel_management.{table_name}(id INT AUTO_INCREMENT PRIMARY KEY, {enter_columns} VARCHAR(255))"
    mycursor.execute(new_table)
    print(f"Table {table_name} created successfully")
    response = input("Do you want to add more Columns (Y/N) : ")
    add_columns(response, table_name)



