from flask import Flask ,jsonify,request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

@app.route("/")
def index():
    # mongo.db.booktickets.insert_one({"a":2})
    return jsonify(massage="simple application")



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


app.run(debug=True)