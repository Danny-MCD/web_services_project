from flask import Flask, jsonify, request, abort
from ActorDAO import ActorDAO

app = Flask(__name__, static_url_path='', static_folder='.')            # Creates a flask app instance

@app.route('/')                                                         # Defines root route, and prints "hello World"
def index():
    return "Hello, World!"

@app.route('/actors')                                                   # Defines route to retieve all actors from the database
def getAll():
    results = ActorDAO.getAll()                                         # Calls the getAll method from ActorDAO, to fetch all actors from database.
    return jsonify(results)                                             # Converts results to JSON format and return them

@app.route('/actors/<int:id>')                                          # Defines a route to retrieve a specific actor by ID
def findById(id):
    foundActor = ActorDAO.findByID(id)                                  # Calls the findByID method from ActorDAO
    return jsonify(foundActor)

@app.route('/actors', methods=['POST'])                                 # Defines route to create a new actor in the database
def create():
    
    if not request.json:                                                # Checks if the request contains JSON data
        abort(400)                                                      # If not it aborts with a 400 Bad request error
    # other checking 
    actor = {                                                           # Extracts filmography, name and age from the JSON request data
        "filmography": request.json['filmography'],
        "name": request.json['name'],
        "age": request.json['age'],
    }
    addedactor = ActorDAO.create(actor)                                 # Call the create method of the ActorDAO
    return jsonify(addedactor)

@app.route('/actors/<int:id>', methods=['PUT'])                         # Defines a route to update the existing actor in the database
def update(id):
    foundActor = ActorDAO.findByID(id)
    if not foundActor:                                                   # If no actor is found abort the request with a 404 Not Found Error
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'age' in reqJson and type(reqJson['age']) is not int:             # Check if the age field is present and is an integer
        abort(400)

    if 'filmography' in reqJson:
        foundActor['filmography'] = reqJson['filmography']
    if 'name' in reqJson:
        foundActor['name'] = reqJson['name']
    if 'age' in reqJson:
        foundActor['age'] = reqJson['age']
    ActorDAO.update(id,foundActor)
    return jsonify(foundActor)
        

@app.route('/actors/<int:id>' , methods=['DELETE'])                       # Define a route to delete an actor from the database
def delete(id):
    ActorDAO.delete(id)
    return jsonify({"done":True})                                         # Return a JSON response indicating that the deletion was sucessful




if __name__ == '__main__' :                                                 # Entry point to run the flask app
    app.run(debug= True)                                                    # Run flask app in debug mode.
