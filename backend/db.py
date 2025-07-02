import os
from pymongo import MongoClient

client = MongoClient(os.getenv("MONGO_URI"))
db = client.ev_recommender
users_collection = db.users
prefs_collection = db.preferences
history_collection = db.history
