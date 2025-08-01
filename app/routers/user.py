from fastapi import APIRouter, HTTPException
from app.models.user import User
from app.schemas.user import UserCreate
from beanie import PydanticObjectId

router = APIRouter()

@router.post("/")
async def create_user(user: UserCreate):
    new_user = User(**user.dict())
    await new_user.insert()
    return new_user

@router.get("/{user_id}")
async def get_user(user_id: PydanticObjectId):
    user = await User.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
