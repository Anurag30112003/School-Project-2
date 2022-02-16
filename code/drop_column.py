from config import mycursor ,mydb

def cdrop():
    table_name = input("Enter table name: ")
    response = input("Enter the column name to be deleted: ")
    mycursor.execute(f"ALTER TABLE {table_name} DROP COLUMN {response}")
    print(f"Column {response} deleted successfully")