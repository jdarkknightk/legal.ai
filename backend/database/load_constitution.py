from pymongo import MongoClient
import json

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.legal_chatbot

# Load JSON File
with open("C:/Users/czar9/legal_chatbot/backend/database/constitution.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Ensure data is a list
if not isinstance(data, list):
    raise TypeError("❌ ERROR: Expected a list, but got a different structure!")

# Insert Data into MongoDB
for part in data:  # Iterate over the list directly
    db.constitution_parts.insert_one(part)

print("✅ Constitution data inserted into MongoDB successfully!")
