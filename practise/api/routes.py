from fastapi import APIRouter, Request

from practise.services.process_user import get_all_users, post_user

router = APIRouter()


@router.get("/users")
async def get_users():
    return get_all_users()


@router.post("/user")
async def insert_users(
    name: str,
    email: str,
    request: Request,
):
    post_user(name, email)
    return {"status": "ok"}
