import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
 database="actors"
)

cursor = db.cursor()
sql="update actor set filmography=%s, name= %s, age=%s  where id = %s"
values = ("purrfect 2","Melanie Scott","18", 7)

cursor.execute(sql, values)

db.commit()
print("update done")

cursor.close()
db.close()
