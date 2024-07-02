import os
from jose import jwt
from jose.exceptions import JWTError

jwt_secret = os.environ.get("JWT_SECRET_KEY", None)


def decode_access_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, jwt_secret, algorithms=['HS256'], options={"verify_aud": False})
        print(payload)
    except JWTError:
        return {}
    return payload


def verify_token(token: str) -> bool:
    payload = decode_token(token)
    return len(payload) > 0
