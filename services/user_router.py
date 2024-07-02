from typing import Annotated
from fastapi import APIRouter
from schemas.user import UserRequest

user_router = APIRouter(prefix="/user", tags=["users"])


@user_router.post("/login")
async def login_user(user_request: UserRequest):
    return {}


@user_router.post("/register")
async def register_user(user_request: UserRequest):
    return {}
