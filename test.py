import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="phpmyadmin",
    password="alicemawuli@2022",  # You should provide the correct password here
    database="test_connection"
)

mycursor = mydb.cursor()

# Create a table called "students"
mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INT)")



# Execute a query to fetch data from the "students" table
mycursor.execute("SELECT * FROM students")

# Fetch and print the results
for db in mycursor:
    print(db)
