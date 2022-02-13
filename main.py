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

sql = ("DELETE FROM customers WHERE address = 'Apple st 652'")

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")