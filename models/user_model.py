from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Boolean, String, DateTime
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
import datetime
import uuid
from database.database import Base
from user.utils.utils import Utils


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "users"

    # user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now())
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=True, nullable=False)
    is_verified = Column(Boolean, default=True, nullable=False)

    __mapper_args__ = {"eager_defaults": True}

    # def __init__(self, *args, **kwargs):
    #     super(User, self).__init__(*args, **kwargs)
    #     self.hashed_password = self.hash_password(Utils())
    #
    # def hash_password(self, utils: Utils):
    #     return utils.get_password_hash(self.hashed_password)
