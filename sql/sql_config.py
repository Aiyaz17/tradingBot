import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

host = os.environ.get('SQL_HOST')
user = os.environ.get('SQL_USER')
password = os.environ.get('SQL_PASS')

# Establishing connection
def connect_db():
    db = mysql.connector.connect(host=host,user = user,password=password)
    return db
    
def execute_and_fetch(query,cursor):
    cursor.execute(query)
    return cursor.fetchall()