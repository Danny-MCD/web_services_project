import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="actors"
)

cursor = db.cursor()
sql="delete from actor where id = %s"
values = (5,)

cursor.execute(sql, values)

db.commit()
print("delete done")

db.close()
cursor.close()