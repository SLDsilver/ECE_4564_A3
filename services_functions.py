from pymongo import MongoClient
from six.moves import input  
from zeroconf import ServiceBrowser, Zeroconf


def get_password(username):
    client = MongoClient('127.0.0.1', 27017)
    db = client['ECE4564_Assignment_3']
    collection = db['service_auth']
    cursor = collection.find({'username': username})
    for document in cursor:
        if document['password']:
            return document['password']
    return ''
