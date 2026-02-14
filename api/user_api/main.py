from fastapi import APIRouter
from database.userservice import *


user_router = APIRouter(prefix="/user", tags=["User API"])



@user_router.post("/add_user")
async def create_user(name: str, email: str, password: str, status: str, 
                        group_id: int = None):
    result = create_user_db(name=name, email=email, password=password, 
                            group_id=group_id, status=status)
    return {"status": 1, "message": result}


