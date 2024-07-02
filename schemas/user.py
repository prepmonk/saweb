from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class UserRequest(BaseModel):
    email: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None


class UserModel(BaseModel):
    id: UUID
    email: Optional[str] = None
    username: Optional[str] = None
