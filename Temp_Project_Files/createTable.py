import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="actors"
)

cursor = db.cursor()
sql="CREATE TABLE actor (id INT AUTO_INCREMENT PRIMARY KEY,filmography VARCHAR(250), name VARCHAR(250), age INT)"

cursor.execute(sql)

db.close()
cursor.close()