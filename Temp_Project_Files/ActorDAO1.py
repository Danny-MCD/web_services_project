# Actor dao 
# this is a demonstration a data layer that connects to a datbase
# Author: Daniel Mc Donagh

import mysql.connector
import dbconfig as cfg
class ActorDAO:
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''
    
    def __init__(self):
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']

    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()
         
    def getAll(self):
        cursor = self.getcursor()
        sql="select * from book"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            #print(result)
            returnArray.append(self.convertToDictionary(result))
        
        self.closeAll()
        return returnArray

    def findByID(self, id):
        cursor = self.getcursor()
        sql="select * from actor where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    def create(self, actor):
        cursor = self.getcursor()
        sql="insert into actor (filmography,name, age) values (%s,%s,%s)"
        values = (actor.get("filmography"), actor.get("name"), actor.get("price"))
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        actor["id"] = newid
        self.closeAll()
        return actor


    def update(self, id, actor):
        cursor = self.getcursor()
        sql="update actor set filmography= %s,name=%s, age=%s  where id = %s"
        
        values = (actor.get("filmography"), actor.get("name"), actor.get("age"),id)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        
    def delete(self, id):
        cursor = self.getcursor()
        sql="delete from actor where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll()
        
        print("delete done")

    def convertToDictionary(self, resultLine):
        attkeys=['id','filmography','name', "age"]
        actor = {}
        currentkey = 0
        for attrib in resultLine:
            actor[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return actor

        
ActorDAO = ActorDAO()