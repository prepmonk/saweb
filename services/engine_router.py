from fastapi import APIRouter, Depends

from schemas.user import UserModel
from security.auth import AuthBearer, get_current_user

engine_router = APIRouter(prefix="/engine", tags=["engine"])


@engine_router.get("/projects", dependencies=[Depends(AuthBearer())])
async def get_projects_list():
    projects = []
    return {"projects": projects}


@engine_router.get("/projects/", dependencies=[Depends(AuthBearer())], tags=["Projects"])
async def retrieve_all_projects_for_user(
        current_user: UserModel = Depends(get_current_user),
):
    """Retrieve all brains for the current user."""
    print(current_user)
    return {}
