import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="actors"
)

cursor = db.cursor()
sql="select * from actor where id = %s"
values = (2,)

cursor.execute(sql, values)
result = cursor.fetchall()
for x in result:
  print(x)

db.close()
cursor.close()

