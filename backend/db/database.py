from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

# Load environment variables



# Initialize MongoDB client
client = MongoClient(MONGO_URI)

# Access the database
db = client.get_database(DATABASE_NAME)
collection = db["Students"]

# Optional: Test connection
try:
    client.admin.command("ping")
    print("Connected to MongoDB!")
except ConnectionFailure:
    print("Failed to connect to MongoDB.")
