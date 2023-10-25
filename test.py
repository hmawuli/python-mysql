import mysql.connector

mydb = mysql.connector.connect(
    host ="localhost",
    user ="phpmyadmin",
    password ="alicemawuli@2022"
    
)

 mycursor = mydb.cursor()
 
#  mycursor.execute("CREATE DATABASE test_connectiondb")

mycursor.execute("SHOW DATABASES")

for dn in mycursor:
    print(db);

  