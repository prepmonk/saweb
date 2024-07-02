from fastapi import APIRouter

engine_router = APIRouter(prefix="/user", tags=["users"])


@engine_router.post("/login")
async def login_user():
    projects = []
    return {"projects": projects}