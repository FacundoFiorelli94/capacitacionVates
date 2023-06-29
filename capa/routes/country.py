from typing import Annotated
from db import get_db
from fastapi import Depends
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from schemas.country import CountryCreate, Country
from models.user import CountryModel
from sqlalchemy.orm import Session

country_router = SQLAlchemyCRUDRouter(
    schema=Country,
    create_schema=CountryCreate,
    db_model=CountryModel,
    db=get_db,
    prefix="/country",
    tags=["Country con crud router"],
    get_one_route=False,
    update_route=False,
    delete_all_route = False
)
