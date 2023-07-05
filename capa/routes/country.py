from typing import Annotated
from db import get_db
from fastapi import Depends
from fastapi_crudrouter import SQLAlchemyCRUDRouter
<<<<<<< HEAD:capa/routers/country.py
from schemas.country import CountryOutput, CountryBase
=======
from schemas.country import CountryCreate, Country
>>>>>>> origin/Franco-crud:capa/routes/country.py
from models.user import CountryModel
from sqlalchemy.orm import Session

country_router = SQLAlchemyCRUDRouter(
<<<<<<< HEAD:capa/routers/country.py
    schema=CountryOutput,
    create_schema=CountryBase,
=======
    schema=Country,
    create_schema=CountryCreate,
>>>>>>> origin/Franco-crud:capa/routes/country.py
    db_model=CountryModel,
    db=get_db,
    prefix="/country",
    tags=["Country con crud router"],
    get_one_route=False,
<<<<<<< HEAD:capa/routers/country.py
    update_route=False
)
=======
    update_route=False,
    delete_all_route = False
)
>>>>>>> origin/Franco-crud:capa/routes/country.py
