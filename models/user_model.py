from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Boolean, String, DateTime
import datetime
import uuid
from database.database import Base
from user.utils import utils


class User(Base, SQLAlchemyBaseUserTable):
    __tablename__ = "users"

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.datetime.now())
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=True)

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.hashed_password = self.hash_password()

    def hash_password(self):
        return utils.get_password_hash(self.hashed_password)
