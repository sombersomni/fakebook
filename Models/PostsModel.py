import pymongo
from pymongo import MongoClient
import bcrypt

class PostsModel:
    def __init__(self, data = None):
        self.client = MongoClient()
        self.db = self.client.socialnetwork
        self.Users = self.db.Users
        self.Posts = self.db.Posts
        self.id = self.insert_post(data) if data != None else None

    def insert_post(self, data):
        return self.Posts.insert({"user_id": data['user_id'], "body": data['postbody']})
    
    def get_posts(self, id):
        posts = self.Posts.find({"user_id": id})
        return [post for post in posts]