import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="",
    password="",  
    database="test_connection"
)

mycursor = mydb.cursor()

#  Execute a query to fetch data from the "students" table
mycursor.execute("SELECT * FROM students")

# Fetch and print the results
for db in mycursor:
    print(db)
