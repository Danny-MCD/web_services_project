import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="actors"
)

cursor = db.cursor()
sql="insert into actor (filmography,name, age) values (%s,%s,%s)"
values = ("Purrfect 2","Mary",21)

cursor.execute(sql, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)

db.close()
cursor.close()