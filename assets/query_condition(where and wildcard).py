import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="phpmyadmin",
    password="alicemawuli@2022",  
    database="test_connection"
)

mycursor = mydb.cursor()

# this is displaying all the age of some of the students
# sql = "SELECT * FROM  students WHERE age = 20"

# this is displaying all the name of the students
# sql = "SELECT * FROM students WHERE  name ='vivian'"

# this is use to fetch all the name that looks like or starts with v(the like command)
sql = "SELECT * FROM students WHERE  name LIKE 'jo%' "

mycursor.execute(sql)

myresult = mycursor.fetchall()

for result in myresult:
    print(result)