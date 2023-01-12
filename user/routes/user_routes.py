from user.schemas.user_schema import UserCreate, UserList
from user.controllers.user_controller import UserController
from auth.jwt_handler import sign_jwt
from fastapi import APIRouter
from typing import List


user_router = APIRouter()


@user_router.post("/create")
async def create_user(body: UserCreate):
    await UserController.create_new_user(body)
    return sign_jwt(body.email)


# todo
@user_router.post("/login")
async def login():
    pass


@user_router.get("/all", response_model=List[UserList])
async def get_users():
    return await UserController.get_all_users()


# todo
@user_router.put("/update/{user_id}")
async def update_user(user_id):
    pass


# todo
@user_router.get("/user/{user_id}")
async def get_current_user(user_id):
    pass


@user_router.delete("/delete/{user_id}")
async def delete_user(user_id):
    return await UserController.delete_spec_user(user_id)
