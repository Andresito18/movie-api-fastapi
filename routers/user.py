from fastapi import APIRouter
from fastapi.responses import JSONResponse
from schemas.user import User
from utils.jwtmanager import create_tocken

user_router = APIRouter()


@user_router.post('/login', tags=['Auth'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token= create_tocken(user.dict())
        return JSONResponse(status_code=200, content=token)