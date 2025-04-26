from fastapi import APIRouter

from practise.services.process_user import get_all_users

router = APIRouter()


@router.get("/users")
async def homepage():
    return get_all_users()
