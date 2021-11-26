import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="ipl"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE cricketers (pos INTEGER AUTO_INCREMENT PRIMARY KEY , Team VARCHAR(255),Name VARCHAR(255),MATCHES INT(10),RUNS INT(10))")