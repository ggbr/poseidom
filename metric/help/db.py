
from pymongo import MongoClient
import pymongo

class Db:

    def __init__(self, collection):
        self._conexao = MongoClient('mongodb://64.251.26.189:27017/')
        self._banco = self._conexao['monitor']
        self._collection = collection

    def setCollection(self, collection):
        self._collection = collection

    # função para insserir um novo registro
    def insert(self, json, collection=''):
        if collection == '':
            col = self._banco[self._collection]
        else:
            col = self._banco[collection]
        post_id = col.insert_one(json).inserted_id
        return post_id

    def select_one(self, json,  collection=''):
        if collection == '':
            col = self._banco[self._collection]
        else:
            col = self._banco[collection]
        return col.find_one(json)
    def select(self, json,  collection=''):
        if collection == '':
            col = self._banco[self._collection]
        else:
            col = self._banco[collection]
        return col.find(json, sort=[('_id', -1), ("servertime", pymongo.DESCENDING)]) 

    # função para retonar o ultimo registro de posição
    def last(self, json,  collection=''):
        if collection == '':
            col = self._banco[self._collection]
        else:
            col = self._banco[collection]
        a = col.find(json, sort=[('_id', -1)]).limit(1)
        return a
    
     # função para retonar o ultimo registro de posição
    def last_one(self, json,  collection=''):
        if collection == '':
            col = self._banco[self._collection]
        else:
            col = self._banco[collection]
        
        a = col.find_one(json, sort=[('_id', -1)])
        return a
