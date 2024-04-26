# flask server that links to a DAO
# author: Andrew Beatty

from flask import Flask, request, jsonify, abort
from ActorDAOskeleton import ActorDAO

app = Flask(__name__)

@app.route('/')
def index():
        return "Hello world"

# getall
# curl http://127.0.0.1:5000/Actors

@app.route('/Actors', methods=['GET'])
def getall():
        return jsonify(ActorDAO.getAll())

# find by id
# curl http://127.0.0.1:5000/actors/1

@app.route('/actors/<int:id>', methods=['GET'])
def findbyid(id):
        return jsonify(ActorDAO.findByID(id))

#create
#curl -X POST -d "{\"filmography\":\"test\", \"name\":\"some guy\", \"age\":123}" http://127.0.0.1:5000/actors
@app.route('/actors', methods=['POST'])
def create():
        # read json from the body
        jsonstring = request.json
        actor = {}

        if "filmography" not in jsonstring:
                abort(403)
        actor["filmography"] = jsonstring["filmography"]
        if "name" not in jsonstring:
                abort(403)
        actor["name"] = jsonstring["name"]
        if "age" not in jsonstring:
                abort(403)
        
        actor["age"] = jsonstring["age"]
        
        return jsonify(ActorDAO.create(actor))

# update
# curl -X PUT -d "{\"filmography\":\"test\", \"name\":\"some guy\", \"age\":123}" http://127.0.0.1:5000/actors/1

@app.route('/actors/<int:id>', methods=['PUT'])
def update(id):
        jsonstring = request.json
        actor = {}

        if "filmography" in jsonstring:
                actor["filmography"] = jsonstring["filmography"]
        if "name" in jsonstring:
                actor["name"] = jsonstring["name"]
        if "age" in jsonstring:
                actor["age"] = jsonstring["age"]
        
        return jsonify(ActorDAO.update(id, actor))

# Delete
# curl -X DELETE  http://127.0.0.1:5000/actors/1

@app.route('/actors/<int:id>', methods=['DELETE'])
def delete(id):
        return jsonify(ActorDAO.delete(id))


if __name__ == "__main__":
    app.run(debug = True)
