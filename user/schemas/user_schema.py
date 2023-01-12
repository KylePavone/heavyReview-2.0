from fastapi import HTTPException
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import validator
import uuid
from user.utils import utils


class TunedModel(BaseModel):
    class Config:
        """Tells pydantic to convert even non-dict obj to json"""

        orm_mode = True


class ShowUser(TunedModel):
    user_id: uuid.UUID
    name: str
    email: EmailStr
    is_active: bool


class UserList(ShowUser):
    pass


class UserCreate(BaseModel):
    name: str
    email: str
    password: str

    @validator("name")
    def validate_name(cls, value):
        if not utils.exp_pattern().match(value):
            raise HTTPException(status_code=422, detail="Имя должно содержать только буквы")
        return value

    @validator("password")
    def validate_password(cls, value):
        if len(value) < 5:
            raise HTTPException(status_code=422, detail="Слишком короткий  пароль")
        return value
