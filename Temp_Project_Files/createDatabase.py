import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root"
)

cursor = db.cursor()

cursor.execute("create DATABASE actors")

db.close()
cursor.close()