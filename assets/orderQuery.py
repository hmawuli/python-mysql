import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "phpmyadmin",
    password = "alicemawuli@2022",
    database = "test_connection"
)

mycursor = mydb.cursor()

#this is for name desc 
#  sql = "SELECT * FROM  students ORDER BY name DESC"

# this is for age desc
# sql = "SELECT * FROM students ORDER BY age DESC"

# this is for name in descending order
sql = "SELECT * FROM students ORDER BY name DESC"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for result in myresult:
    print(result)