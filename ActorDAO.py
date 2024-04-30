# ActorDAO - (Data Access Object)
# Author: Daniel Mc Donagh

import mysql.connector
import dbconfig as cfg

class actorDAO:                                     # Defines the class for accessing the actor data in the database
    connection =""                                  # Initialises the class variables
    cursor =""
    host =""
    user =""
    password =""
    database =""

    

    def __init__(self):                             # Constructor method for initialising the object
        self.host=       cfg.mysql['host']          # Assignment of values from configuration file
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']
    
    def getCursor(self):                             # Method to establish a database connection and return a cursor object
        self.connection = mysql.connector.connect(   # Connect to database using assigned credentials
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()       # Creates a cursor object for execution of SQL queries
        return self.cursor
    
    def closeAll(self):                              # Method to close the database object and cursor
        self.connection.close()                      # Close database connection
        self.cursor.close()                          # Close cursor
    
    
    def getAll(self):                                # Method to retrieve all actors from database
        cursor = self.getCursor()                    # Get cursor object
        sql="select * from actor"                    # Define SQL query
        cursor.execute(sql)                          # Execute SQL query
        results = cursor.fetchall()                  # Fetch all results from query
        returnArray = []                             # Initialises an empty list to store results
        for result in results:                       # Interates through results
            returnArray.append(self.convertToDictionary(result))            # Converts each result to a dictionary object and appends to the list.

        self.closeAll()                              # Close database connection and cursor
        return returnArray

    def findByID(self, id):                          # Method to retrieve an actor by ID from the database
        cursor = self.getCursor()
        sql="select * from actor where id = %s"
        values = (id,)                               # Defines a tuple containing the ID value

        cursor.execute(sql, values)
        result = cursor.fetchone()                  # Fetch one result from the query
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue
    
    def create(self, actor):                         # Method to create a new actor in the database
        cursor = self.getCursor()
        sql="insert into actor (filmography, name, age) values (%s,%s,%s)"
        values = (actor.get("filmography"), actor.get("name"), actor.get("age"))
        cursor.execute(sql, values )

        self.connection.commit()                     # Commit the transaction
        newid = cursor.lastrowid                     # Get the ID of the new actor
        actor["id"] = newid                          # Update actor dictionary with the new ID
        self.closeAll()
        return actor


    def update(self, id,  actor):                    # Method to update an existing actor in the database
        cursor = self.getCursor()
        sql="update actor set filmography=%s, name= %s, age=%s  where id = %s"
        print(f"update actor {actor}")
        values = (actor.get("filmography"), actor.get("name"), actor.get("age"), id)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        

    def delete(self, id):                            # Method to delete an actor from the database
        cursor = self.getCursor()
        sql="delete from actor where id = %s"
        values = (id,)
        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll
        print("delete done")
        

    def convertToDictionary(self, result):            # Method to convert a result tuple to a dictionary object
        actorKeys = ["id", "filmography", "name", "age"]
        actor = {}                                    # Initialise an empty dictionary object
        currentkey = 0                                # Variable to track current key index
        for attrib in result:                         # Iterate through the result tuple
            actor[actorKeys[currentkey]] = attrib     # Assign attribute to corresponding key in dictionary
            currentkey = currentkey + 1 
        return actor

ActorDAO = actorDAO()                                 # Create an instance of the actorDAO class for accessing actor data