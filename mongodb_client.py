from pymongo import MongoClient
from urllib.parse import quote_plus

client = MongoClient("mongodb://user:asdasdasdasdasdasdad@localhost:27017/?authSource=mydb")
db = client["mydb"]
print(db.list_collection_names())
