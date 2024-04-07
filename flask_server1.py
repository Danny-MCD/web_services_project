# very simple flask server

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
        return "Hello world"

@app.route('/Actors', methods=['GET'])
def getall():
        return "getall"

@app.route('/Actors/<int:ID>', methods=['GET'])
def FindbyID():
        return "FindbyID"

@app.route('/Actors', methods=['POST'])
def Create():
        jsonstring = request.json
        return f"Create{jsonstring}"

@app.route('/Actors/<int:ID>', methods=['PUT'])
def Update(ID): 
        jsonstring = request.json
        return f"Update{ID}{jsonstring}"

@app.route('/Actors/ID', methods=['DELETE'])
def Delete():
        return f"Delete{ID}"

if __name__ == "__main__":
    app.run(debug = True)

# getall
# curl http://127.0.0.1:5000/books