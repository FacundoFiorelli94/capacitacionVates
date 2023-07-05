from typing import Annotated
from db import get_db
from fastapi import Depends
from fastapi_crudrouter import SQLAlchemyCRUDRouter
<<<<<<< HEAD:capa/routers/language.py
from schemas.language import LanguageOutput, LanguageBase
from models.user import LanguageModel
from sqlalchemy.orm import Session



language_router = SQLAlchemyCRUDRouter(
    schema=LanguageOutput,
    create_schema=LanguageBase,
=======
from schemas.language import Language, LanguageCreate
from models.user import LanguageModel
from sqlalchemy.orm import Session

language_router = SQLAlchemyCRUDRouter(
    schema=Language,
    create_schema=LanguageCreate,
>>>>>>> origin/Franco-crud:capa/routes/language.py
    db_model=LanguageModel,
    db=get_db,
    prefix="/language",
    tags=["Language con crud router"],
    get_one_route=False,
<<<<<<< HEAD:capa/routers/language.py
    update_route=False
=======
    update_route=False,
    delete_all_route = False
>>>>>>> origin/Franco-crud:capa/routes/language.py
)