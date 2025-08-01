import os
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
from app.models.user import User
from app.models.product import Product

load_dotenv()

async def init_db():
    client = AsyncIOMotorClient(os.getenv("MONGODB_URI"))
    db = client.get_default_database()
    await init_beanie(database=db, document_models=[User, Product])
