from pymongo import MongoClient
from mongo.config import settings

client = MongoClient(f"mongodb+srv://{settings.MONGO_USERNAME}:{settings.MONGO_PASSWORD}@{settings.MONGO_CLUSTER}?retryWrites=true&w=majority")

db = client[settings.MONGO_DB_NAME]