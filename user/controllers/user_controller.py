from sqlalchemy import select, delete, update
from models.user_model import User
from user.schemas.user_schema import UserCreate
from user.utils.utils import Utils


class UserController:
    def __init__(self, db_session):
        self.db_session = db_session

    async def create_user(self, body):
        async with self.db_session() as session:
            async with session.begin():
                check_user = await self.get_user_by_email(body.email)
                if check_user:
                    return 0
                new_user = User(name=body.name, email=body.email, hashed_password=body.password)
                session.add(new_user)
                return await session.flush()

    async def login_user(self, email):
        async with self.db_session() as session:
            async with session.begin():
                check_user = await self.get_user_by_email(email)
                if check_user:
                    return check_user

    async def get_user_by_id(self, user_id):
        async with self.db_session() as session:
            async with session.begin():
                user = await session.execute(select(User.user_id, User.name, User.email).where(User.user_id == user_id))
                return user.first()

    async def get_user_by_email(self, email):
        async with self.db_session() as session:
            async with session.begin():
                user = await session.execute(select(User.user_id, User.name, User.email, User.hashed_password)
                                             .where(User.email == email))
                return user.first()

    async def get_all_users(self):
        async with self.db_session() as session:
            async with session.begin():
                users = await session.execute(select(User.user_id, User.name, User.email, User.is_active))
                result = [dict(user) for user in users]
                return result

    async def update_user(self, user_id, body: UserCreate, utils: Utils):
        async with self.db_session() as session:
            async with session.begin():
                user = await session.execute(select(User).where(User.user_id == user_id))
                result = user.first()
                if not result:
                    return 0
                update_user = update(User).values(
                    {
                        "name": body.name,
                        "email": body.email,
                        "hashed_password": utils.get_password_hash(body.password)
                     }
                ).where(User.user_id == user_id)
                return await session.execute(update_user)

    async def delete_user(self, user_id):
        async with self.db_session() as session:
            async with session.begin():
                return await session.execute(delete(User).where(User.user_id == user_id))
