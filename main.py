from flask import Flask ,jsonify,request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

@app.route("/")
def index():
    # mongo.db.booktickets.insert_one({"a":2})
    return jsonify(message="simple application")



@app.route("/data", methods=['POST'])
def createData():
    databaseCollection=mongo.db.data
    name=request.json["name"]
    description=request.json["description"]
    dataId=databaseCollection.insert_one({'name':name,'description':description}).inserted_id
    newData=databaseCollection.find_one({"_id":dataId})
    return jsonify(name=newData['name'], descriptionn=newData['description'])
    

@app.route("/data/getdata", methods=["GET"])
def getdata():
    databaseCollection=mongo.db.data
    data=[]
    for d in databaseCollection.find():
        data.append({'name': d['name'], 'description': d['description']})
    
    return jsonify(data)


@app.route("/data/<name>",methods=['PUT'])
def updateData(name):
    databaseCollection=mongo.db.data
    data=databaseCollection.find_one_and_update({"name": "name"},{"$set":request.json},return_document=True)
    if data:
        return jsonify(name=data['name'], descriptionn=data['description'])
    return jsonify(message="data not found"),404




app.run(debug=True)