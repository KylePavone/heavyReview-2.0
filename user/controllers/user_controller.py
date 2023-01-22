# from sqlalchemy import select, delete, update
# from models.user_model import User
# from user.utils.utils import Utils
# from database.database import AsyncSession


# class UserController:

    # async def create_user(self, body, session: AsyncSession):
    #     new_user = User(name=body.name, email=body.email, hashed_password=body.password)
    #     session.add(new_user)
    #     return new_user

    # async def login_user(self, email: str, session: AsyncSession):
    #     check_user = await self.get_user_by_email(email, session)
    #     if check_user:
    #         return check_user

    # async def get_user_by_id(self, user_id, session):
    #     user = await session.execute(select(User.id, User.name, User.email).where(User.id == user_id))
    #     return user.first()
    #
    # async def get_user_by_email(self, email: str, session: AsyncSession):
    #     user = await session.execute(select(User.user_id, User.name, User.email, User.hashed_password)
    #                                  .where(User.email == email))
    #     return user.first()
    #
    # async def get_all_users(self, session: AsyncSession):
    #     return await session.execute(select(User.user_id, User.name, User.email, User.is_active))
    #
    # async def update_user(self, user_id, body, utils: Utils, session: AsyncSession):
    #     update_user = update(User).values(
    #         {
    #             "name": body.name,
    #             "email": body.email,
    #             "hashed_password": utils.get_password_hash(body.password)
    #          }
    #     ).where(User.id == user_id)
    #     return await session.execute(update_user)
    #
    # async def delete_user(self, user_id, session: AsyncSession):
    #     return await session.execute(delete(User).where(User.user_id == user_id))
