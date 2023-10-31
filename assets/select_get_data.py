import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="",
    password="",  
    database="test_connection"
)

mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM students")

# we want to fetch all the age

mycursor.execute("SELECT age FROM students")

myresult = mycursor.fetchall()

for row in myresult:
    print(row)