import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

USER = os.getenv("MONGOUSERNAME")
PASSWORD = os.getenv("MONGOPASSWORD")

MONGODB_URL = f"mongodb+srv://{USER}:{PASSWORD}@cluster0.fojn3vj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = AsyncIOMotorClient(MONGODB_URL)
db = client.college
student_collection = db.get_collection("students")
user_collection = db.get_collection("users")
account_details_collection = db.get_collection("accountDetails")