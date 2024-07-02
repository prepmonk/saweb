from fastapi import APIRouter, Depends

from logger import get_logger
from schemas.user import UserModel
from security.auth import AuthBearer, get_current_user

engine_router = APIRouter(prefix="/engine", tags=["engine"])

logger = get_logger(__name__)


@engine_router.get("/projects/")  #dependencies=[Depends(AuthBearer())])
async def retrieve_all_projects_for_user(
        current_user: UserModel = Depends(get_current_user),
):
    """Retrieve all brains for the current user."""
    logger.info(current_user)
    return {}
