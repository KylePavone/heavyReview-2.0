from passlib.context import CryptContext
import re


class Utils:
    PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def get_password_hash(self, password: str):
        return self.PWD_CONTEXT.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str):
        return self.PWD_CONTEXT.verify(plain_password, hashed_password)

    @staticmethod
    def exp_pattern():
        pattern = re.compile(r"^[а-яА-Яa-zA-Z\-]+$")
        return pattern
