from flask import Flask
from flask import jsonify

import pymongo
from pymongo import MongoClient
client = MongoClient()
client = MongoClient('mongodb://mongodb:27017/')
app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'monitor'
app.config['MONGO_URI'] = 'mongodb://mongodb:27017/'

db = client['monitor']
collection = db['status']
@app.route('/')
def hello_world():
    status = collection.find_one()
    print(status)
    json = {}

    json["cpu"] = status['cpu']
    json["memoria"] = status['memoria']


    
    return jsonify({'result' : json})

# exemplo 
#http://127.0.0.1:8081/api/v1/device/344496
@app.route('/api/v1/status')
def json():
    position = db.last_one({'cpu': 0})
    if position == None:
        return jsonify({'result' : 'Erro id não encontrado' , 'dados': 0 }),400
     #json = {'modelo' : s['modelo'], 'date' : s['date']}
    json = {}

    json["cpu"] = position[0]['cpu']
    json["memoria"] = position[0]['memoria']


    
    return jsonify({'result' : json})