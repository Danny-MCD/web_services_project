# Actor dao skeleton
# this is a demonstration of the type of function a data layer might have
# Author: Daniel Mc Donagh

class ActorDAO:
    # get all          
    def getAll(self):
        #TODO implement
        return [{"id":1,"filmography":"blah","name":"Liya Silver","age":23}]
    # find by id
    def findByID(self, id):
        return {"id":1,"filmography":"blah","name":"Liya Silver","age":23}
    # create a actor
    def create(self, actor):
        return {"id":1,"filmography":"blah","name":"Liya Silver","age":23}
    #update a actor
    def update(self,id , actor):
        return {"id":1,"filmography":"blah","name":"someone","age":23}
    # delete a actor of a given id    
    def delete(self, id):
        return True
        
ActorDAO = ActorDAO()

if __name__ == "__main__":
    book = {"id":1,"filmography":"blah","name":"Liya Silver","age":23} 
    print ("test getall")
    print (f"\t{ActorDAO.getAll()}")
    print ("test findById(1)")
    print (f"\t{ActorDAO.findByID(1)}")
    print ("test create")
    print (f"\t{ActorDAO.create(actor)}")
    print ("test update")
    print (f"\t{ActorDAO.update(1,actor)}")
    print ("test delete")
    print (f"\t{ActorDAO.delete(1)}")
   
