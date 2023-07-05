from typing import Annotated
from db import get_db
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from schemas.language import LanguageOutput, LanguageBase
from models.user import LanguageModel



language_router = SQLAlchemyCRUDRouter(
    schema=LanguageOutput,
    create_schema=LanguageBase,
    db_model=LanguageModel,
    db=get_db,
    prefix="/language",
    tags=["Language con crud router"],
    get_one_route=False,
    update_route=False
)