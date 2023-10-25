import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "phpmyadmin",
    password = "alicemawuli@2022",
    database = "test_connection"
)

mycursor = mydb.cursor()
# this is how we delete aget
# sql = "DELETE FROM students WHERE age = 19 "

# how to delete or drop a table
sql = "DROP TABLE IF EXISTS students"
mycursor.execute(sql)

mydb.commit()