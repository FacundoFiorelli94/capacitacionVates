from fastapi import APIRouter
from db import get_db
from models.user import UserModel
from schemas.auth.user import CreateUserRequest, UserOutPut
from fastapi_crudrouter import SQLAlchemyCRUDRouter

user_router = SQLAlchemyCRUDRouter(
    schema=UserOutPut,
    create_schema=CreateUserRequest,
    db_model=UserModel,
    db=get_db,
    prefix="/user",
    tags=["User"]
)

