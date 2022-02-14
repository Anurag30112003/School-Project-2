import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()
password = os.getenv("PASSWORD")
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=f'{password}',
    database="hotel_management"
)
mycursor = mydb.cursor()
