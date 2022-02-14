from config import mycursor, mydb
from columns_add import add_columns
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



