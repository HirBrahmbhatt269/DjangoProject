# Using this file you will be able to create your database using python
# You can even set it up using the mysql workbench or server as well!
import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password="I@mzuzu26936",
    auth_plugin='mysql_native_password'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE elderco")

print("Database has been created")
