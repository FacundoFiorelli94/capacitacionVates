from db import get_db
from fastapi import APIRouter
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from models.user import UserModel
from schemas.auth.user import CreateUserRequest, UserOutput

user_router = SQLAlchemyCRUDRouter(
    schema=UserOutput,
    create_schema=CreateUserRequest,
    db_model=UserModel,
    db=get_db,
    prefix="/user",
    tags=["User con crud router"],
    create_route=False,
    update_route=False,
    get_one_route=False,
    delete_one_route=False,
)