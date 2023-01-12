import time
import jwt
import settings


JWT_SECRET = settings.SECRET

JWT_ALGORITHM = settings.ALGORITHM


def token_response(token: str):
    """ Returns generated tokens """

    return {
        "access_token": token
    }


def sign_jwt(user_id: str):
    """ Used for signing JWT """
    payload = {
        "user_id": user_id,
        "expiry": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)


def decode_jwt(token: str):
    """ Decode jwt_token """

    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
        return decode_token if decode_token["expires"] >= time.time() else None
    except:
        return {}

