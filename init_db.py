from pymongo import MongoClient

client = MongoClient('127.0.0.1', 27017)
db = client.ECE4564_Assignment_3
post = {
        "username": "Bud_Barclay",
        "password": "Polar-Ray_Dynasphere"
        }
db.service_auth.insert_one(post)
