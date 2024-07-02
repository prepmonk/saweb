from typing import Optional

from fastapi import Request, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from schemas.user import UserModel
from security.jwt_middleware import verify_token, decode_access_token


class AuthBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: Optional[HTTPAuthorizationCredentials] = await super().__call__(request)
        print(credentials)
        if credentials and credentials.scheme == 'Bearer':
            raise HTTPException(status_code=401, detail="Token must be Bearer")
        elif not credentials:
            raise HTTPException(
                status_code=403, detail="Authentication credentials missing"
            )
        token = credentials.credentials
        print(token)
        return await self.authenticate(token)

    async def authenticate(self, token: str) -> UserModel:
        print(f"authenticate = {token}")
        if verify_token(token):
            return decode_access_token(token)

        return None


def get_current_user(user: UserModel = Depends(AuthBearer())) -> UserModel:
    return user
