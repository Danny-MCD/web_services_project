import mysql.connector
class ActorDAO:
    host =""
    user = ""
    password =""
    database =""

    connection = ""
    cursor =""

    def __init__(self): 
        #these should be read from a config file
        self.host="localhost"
        self.user="root"
        self.password=""
        self.database="actor"
    
    def getCursor(self): 
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def closeAll(self):
        self.connection.close()
        self.cursor.close()
    
    
    def getAll(self):
        cursor = self.getCursor()
        sql="select * from actor"
        cursor.execute(sql)
        result = cursor.fetchall()
        actorlist = []
        for row in result:
            actorlist.append(self.convertToDict(row))

        self.closeAll()
        return actorlist

    def findByID(self, id):
        cursor = self.getCursor()
        sql="select * from actor where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        self.closeAll()
        return self.convertToDict(result)
    
    def create(self, actor):
        cursor = self.getCursor()
        sql="insert into actor (filmography,name, age) values (%s,%s,%s)"
        values = (actor.get("name"), student.get("age"))
        cursor.execute(sql, values )

        self.connection.commit()
        newid = cursor.lastrowid
        actor["id"] = newid
        self.closeAll()
        return actor


    def update(self, id,  actor):
        cursor = self.getCursor()
        sql="update actor set filmography=%s, name= %s, age=%s  where id = %s"
    
        values = (actor.get("filmography"), actor.get("name"), actor.get("age"), id)
        cursor.execute(sql, values)
        self.connection.commit()
        
        self.closeAll()
        return actor

    def delete(self, id):
        cursor = self.getCursor()
        sql="delete from actor where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll
        #print("delete done")
        return True

    def convertToDict(self,resultLine):
        actorKeys = ["id", "filmography", "name", "age"]
        currentkey = 0
        actor = {}
        for attrib in resultLine:
            actor[actorKeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return actor

ActorDAO = ActorDAO()