import pymongo
from pymongo import MongoClient
import bcrypt

class RegisterModel:
    def __init__(self, data):
        self.client = MongoClient()
        self.db = self.client.socialnetwork
        self.Users = self.db.Users
        self.id = self.insert_user(data)
    
    def insert_user(self, data):
        hashed = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt())
        id = self.Users.insert({"username": data.username,
                                "name": data.name,
                                "email": data.email,
                                "password": hashed})

        user = self.Users.find_one({"username": data.username})
        if bcrypt.checkpw("avacodo1".encode(), user['password']):
            print("password matches")

        return id
