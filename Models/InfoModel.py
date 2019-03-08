import pymongo
from pymongo import MongoClient

class InfoModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.socialnetwork
        self.UserInfo = self.db.UserInfo
        self.id = None
    def insert_info(self, data):
        self.id = self.UserInfo.insert({"user_id": data['user_id'],
                            "about": data['about'],
                            "hobbies": data['hobbies'],
                            "birthday": data['birthday'],
                            "professional": data['professional'],
                            "avatar": data['avatar']})

        return True
    def get_info(self, data):
        info = self.UsersInfo.find_one({"user_id": data['user_id']})
        return info