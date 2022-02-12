# Hotel Manangement system in python with mysql database.
import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()
PASS = os.getenv('PASSWORD')
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = f"{PASS}",
    database="mydatabase"
)
mycursor = mydb.cursor()

# sql = "INSERT INTO customers (name, address) VALUES ('Raju', 'Dolakpur')"
# # val = ("John", "Highway 21")
# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")

for i in range(10):
    print(help(mycursor))