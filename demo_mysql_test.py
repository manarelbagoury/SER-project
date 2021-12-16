import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Amsotired!!",
  database="testdatabase"
)

mycursor = mydb.cursor()


#mycursor.execute("CREATE TABLE Person2 (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
#mycursor.execute("INSERT INTO Person2 (name, age) VALUES (%s,%s)", ('Manar', 19))
#mydb.commit()
mycursor.execute("SELECT * FROM testdatabase.person2")

for x in mycursor:
    print(x)