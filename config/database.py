
from pymongo.mongo_client import MongoClient

client = MongoClient("mongodb://venkatesh:venkatesh@localhost:27017/?authMechanism=DEFAULT")
db = client["todo_db"]
collections_name = db["todo_collections"]
