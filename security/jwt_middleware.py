import os

from jose import jwt
from jose.exceptions import JWTError

from logger import get_logger
from schemas.user import UserModel

jwt_secret = os.environ.get("JWT_SECRET_KEY", None)
ALGORITHM = 'HS256'

logger = get_logger(__name__)


def decode_access_token(token: str) -> UserModel:
    try:
        payload = jwt.decode(token, jwt_secret, algorithms=[ALGORITHM], options={"verify_aud": False})
        return UserModel(id=payload.get('sub'), **payload)
    except JWTError as err:
        import traceback
        print(traceback.format_exc())
        logger.error(f"Exception: {str(err)} ")
    return None

