from passlib.context import CryptContext
import re


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def exp_pattern():
    pattern = re.compile(r"^[а-яА-Яa-zA-Z\-]+$")
    return pattern
