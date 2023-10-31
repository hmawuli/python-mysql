import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user ="",
    password = "",
    database = "test_connection"
)

mycursor = mydb.cursor()
# this is the update function
# sql = "UPDATE students SET age = 19 WHERE name = 'Bob'"

# this is for the limit command 
mycursor.execute("SELECT * FROM students LIMIT 3 OFFSET 2")

myresult = mycursor.fetchall()

for result in myresult:
    print(result)
