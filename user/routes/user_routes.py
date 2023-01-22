# from user.schemas.user_schema import UserCreate, ShowUser, UserLogin
# from user.controllers.user_controller import UserController
# from fastapi import HTTPException, Depends
# from classy_fastapi import Routable, get, delete, post, put
# from user.utils.utils import Utils
# from typing import List
# from database.database import get_session
#
#
# class UserRoutes(Routable):
#
#     def __init__(self, uc: UserController):
#         super().__init__()
#         self.__uc = uc

    # @post("/create")
    # async def create_user(self, body: UserCreate, session=Depends(get_session)):
    #     await self.__uc.create_user(body, session)
    #     await session.commit()
    #     new_user = {
    #         "name": body.name,
    #         "email": body.email,
    #     }
    #     user_info = {**new_user, **sign_jwt(body.email)}
    #     return user_info

    # @post("/login")
    # async def login(self, body: UserLogin, session=Depends(get_session)):
    #     current_user = await self.__uc.login_user(body.email, session)
    #     await session.commit()
    #     if not current_user:
    #         raise HTTPException(status_code=401, detail="Invalid email")
    #     utils = Utils()
    #     if utils.verify_password(body.password, current_user.hashed_password):
    #         return sign_jwt(body.email)
    #     raise HTTPException(status_code=401, detail="Invalid password")

    # @get("/{user_id}", response_model=ShowUser)
    # async def get_user_by_id(self, user_id, session=Depends(get_session)):
    #     current_user = await self.__uc.get_user_by_id(user_id, session)
    #     if not current_user:
    #         raise HTTPException(status_code=404, detail="User not found")
    #     return ShowUser(
    #         user_id=current_user.user_id,
    #         name=current_user.name,
    #         email=current_user.email,
    #         is_active=True
    #     )

    # @post("/email")
    # async def get_user_by_email(self, email: str, session=Depends(get_session)):
    #     current_user = await self.__uc.get_user_by_email(email, session)
    #     if not current_user:
    #         raise HTTPException(status_code=404, detail="User not found")
    #     return ShowUser(
    #         user_id=current_user.user_id,
    #         name=current_user.name,
    #         email=current_user.email,
    #         is_active=True
    #     )

    # @get("/", response_model=List[ShowUser])
    # async def get_all_users(self, session=Depends(get_session)):
    #     users = await self.__uc.get_all_users(session)
    #     return [dict(user) for user in users]
    #
    # @put("/update/{user_id}", response_model=ShowUser)
    # async def update_user(self, user_id, body: UserCreate, session=Depends(get_session)):
    #     current_user = await self.__uc.get_user_by_id(user_id, session)
    #     if not current_user:
    #         raise HTTPException(status_code=404, detail="User not found")
    #     utils = Utils()
    #     await self.__uc.update_user(user_id, body, utils, session)
    #     await session.commit()
    #     return ShowUser(
    #         user_id=user_id,
    #         name=body.name,
    #         email=body.email,
    #         is_active=True
    #     )
    #
    # @delete("/delete/{user_id}")
    # async def delete_user(self, user_id, session=Depends(get_session)):
    #     current_user = await self.__uc.get_user_by_id(user_id, session)
    #     if not current_user:
    #         raise HTTPException(status_code=404, detail="User not found")
    #     await self.__uc.delete_user(user_id, session)
    #     await session.commit()
    #     return {"user": user_id, "deleted": True}
