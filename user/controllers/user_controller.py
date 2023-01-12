from user.schemas.user_schema import ShowUser
from sqlalchemy import select, delete, update
from models.user_model import User
from database.database import async_session


class UserController:

    @staticmethod
    async def create_new_user(body):
        async with async_session() as session:
            async with session.begin():
                new_user = User(name=body.name, email=body.email, hashed_password=body.password)
                session.add(new_user)
                await session.flush()
                return ShowUser(
                    user_id=new_user.user_id,
                    name=new_user.name,
                    email=new_user.email,
                    is_active=new_user.is_active
                )

    @staticmethod
    async def get_all_users():
        async with async_session() as session:
            async with session.begin():
                users = await session.execute(select(User.user_id, User.name, User.email, User.is_active))
                result = [dict(user) for user in users]
                return result

    # @staticmethod
    # async def update_user():
    #     async with async_session() as session:
    #         async with session.begin():
    #             pass

    @staticmethod
    async def delete_spec_user(user_id):
        async with async_session() as session:
            async with session.begin():
                await session.execute(delete(User).where(User.user_id == user_id))
                return "Done"
