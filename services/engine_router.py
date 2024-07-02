from fastapi import APIRouter, Depends

from security.auth import AuthBearer

engine_router = APIRouter(prefix="/engine", tags=["engine"])


@engine_router.get("/projects", dependencies=[Depends[AuthBearer()]])
async def get_projects_list():
    projects = []
    return {"projects": projects}
