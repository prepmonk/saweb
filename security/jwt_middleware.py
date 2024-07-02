import os
from pprint import pprint

from jose import jwt
from jose.exceptions import JWTError

from schemas.user import UserModel

jwt_secret = os.environ.get("JWT_SECRET_KEY", None)
ALGORITHM = 'HS256'


def decode_access_token(token: str) -> UserModel:
    try:
        payload = jwt.decode(token, jwt_secret, algorithms=[ALGORITHM], options={"verify_aud": False})
    except JWTError:
        return None
    return UserModel(id=payload.get('sub'), **payload)

