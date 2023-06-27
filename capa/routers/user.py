from typing import Annotated

from db import get_db
from fastapi import Depends
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from models.user import CountryModel, LanguageModel, UserModel
from schemas.auth.user import CreateUserRequest, UserOutput
from sqlalchemy.orm import Session

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


#get by company con nombre country y nombre de lenguaje
#get all con nombre country y nombre de lenguaje
#put con inhabilitación de usuario

# async def get_user_by_country(country_name: str, db: Annotated[Session, Depends(get_db)]):
#     country = country_name.upper()
#     return db.query(UserModel).filter(CountryModel.country_name == country).all()

# async def get_user_by_language(language: str,db: Annotated[Session, Depends(get_db)]):
#     language = language.upper()
#     return db.query(UserModel).filter(LanguageModel.language_name == language).all()
    

