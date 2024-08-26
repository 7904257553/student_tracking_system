from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from Schema import Trained_Student, Located_Student
import os
from dotenv import dotenv_values

config = dotenv_values(os.path.join(os.getcwd(), ".env"))

uri = config["MONGO_URI"]

client = MongoClient(uri, server_api=ServerApi('1'))

class Students:
    def __init__(self):
        self.db = client["tracking"]
        self.collection = self.db["student"]

    def insert_one(self, student: Trained_Student):
        existing_student = self.find_one(student)
        if existing_student is None:
            return self.collection.insert_one({"name": student.name, "location": "Not Found"})
        else:
            return None

    def find_one(self, student: Trained_Student):
        return self.collection.find_one({"name": student.name}, {"_id":0 })

    def find_cam(self, camID: str):
        return self.collection.find({"location": camID}, {"_id":0, "location": 0})
    
    def uptadte_location(self, student: Located_Student ):
        return self.collection.update_one({"name": student.name}, {"$set": {"location": student.location}})
