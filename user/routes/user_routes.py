from user.schemas.user_schema import UserCreate, ShowUser, UserLogin
from user.controllers.user_controller import UserController
from auth.jwt_handler import sign_jwt
from fastapi import HTTPException, Depends
from classy_fastapi import Routable, get, delete, post, put
from user.utils.utils import Utils
from auth.jwt_bearer import JWTBearer


class UserRoutes(Routable):

    def __init__(self, uc: UserController):
        super().__init__()
        self.__uc = uc

    @post("/create")
    async def create_user(self, body: UserCreate):
        new_user = await self.__uc.create_user(body)
        if new_user == 0:
            raise HTTPException(status_code=400, detail="Email already registered")
        new_user = {
            "name": body.name,
            "email": body.email,
        }
        user_info = {**new_user, **sign_jwt(body.email)}
        return user_info

    @post("/login")
    async def login(self, body: UserLogin):
        current_user = await self.__uc.login_user(body.email)
        if not current_user:
            raise HTTPException(status_code=401, detail="Invalid email")
        utils = Utils()
        if utils.verify_password(body.password, current_user.hashed_password):
            return sign_jwt(body.email)
        raise HTTPException(status_code=401, detail="Invalid password")

    @get("/{user_id}", response_model=ShowUser)
    async def get_user_by_id(self, user_id):
        current_user = await self.__uc.get_user_by_id(user_id)
        if not current_user:
            raise HTTPException(status_code=404, detail="User not found")
        return ShowUser(
            user_id=current_user.user_id,
            name=current_user.name,
            email=current_user.email,
            is_active=True
        )

    @get("/email")
    async def get_user_by_email(self, email):
        current_user = await self.__uc.get_user_by_email(email)
        if not current_user:
            raise HTTPException(status_code=404, detail="User not found")
        return ShowUser(
            user_id=current_user.user_id,
            name=current_user.name,
            email=current_user.email,
            is_active=True
        )

    @get("/")
    async def get_all_users(self):
        return await self.__uc.get_all_users()

    @put("/update/{user_id}", dependencies=[Depends(JWTBearer())], response_model=ShowUser)
    async def update_user(self, user_id, body: UserCreate):
        current_user = await self.__uc.get_user_by_id(user_id)
        if not current_user:
            raise HTTPException(status_code=404, detail="User not found")
        utils = Utils()
        await self.__uc.update_user(user_id, body, utils)
        return ShowUser(
            user_id=user_id,
            name=body.name,
            email=body.email,
            is_active=True
        )

    @delete("/delete/{user_id}", dependencies=[Depends(JWTBearer())])
    async def delete_user(self, user_id):
        current_user = await self.__uc.get_user_by_id(user_id)
        if not current_user:
            raise HTTPException(status_code=404, detail="User not found")
        await self.__uc.delete_user(user_id)
        return {"user": user_id, "deleted": True}
