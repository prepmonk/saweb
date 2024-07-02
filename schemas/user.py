from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class UserRequest(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None


class UserModel(BaseModel):
    id: UUID
    email: Optional[str]
    aud: Optional[str] = None
    exp: Optional[int] = None
    iat: Optional[int] = None
    iss: Optional[str] = None
    sub: Optional[UUID] = None
    phone: Optional[str] = None
    app_metadata: Optional[dict] = None
    providers: Optional[str] = None
    user_metadata: Optional[dict] = None
    role: Optional[str] = None
    aal: Optional[str] = None
    amr: Optional[list[dict]] = None
    session_id: Optional[str] = None

