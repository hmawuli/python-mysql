import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="phpmyadmin",
    password="alicemawuli@2022",  
    database="test_connection"
)

mycursor = mydb.cursor()

sqlFormal = "INSERT INTO students (name, age) VALUE (%s, %s)"
students =[("job", 12),
           ("joseph", 22),
           ("vivian", 20),
           ("yayara", 19),
           ("asha", 20),
           ]

mycursor.executemany(sqlFormal, students)

mydb.commit()