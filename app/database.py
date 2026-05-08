from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings

class MongoDB:
    client: AsyncIOMotorClient = None
    db = None

mongo = MongoDB()

async def connect_to_mongo():
    mongo.client = AsyncIOMotorClient(settings.MONGO_URI)
    mongo.db = mongo.client.get_default_database()
    print("Connected to MongoDB!")

async def close_mongo_connection():
    mongo.client.close()
    print("MongoDB connection closed.")