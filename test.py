import mysql.connector

mydb = mysql.connector.connect(
    host ="localhost",
    user ="phpmyadmin",
    password ="alicemawuli@2022"
    
)

 mycursor = mydb.cursor()
 
#  mycursor.execute("CREATE DATABASE test_connectiondb")

# mycursor.execute("SHOW DATABASES")

#
mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10),)")

   for db in mycursor:
       
   print(db)
