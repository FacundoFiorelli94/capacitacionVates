from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from db import get_db
from models.user import UserModel, CountryModel, LanguageModel
from schemas.user_crud import UserOutput
from schemas.country import UserOutputCountry
from schemas.language import UserOutputLanguage
from sqlalchemy.orm import Session


user_router = APIRouter(
  prefix='/user',
  tags=['user'],
)


@user_router.get('/', status_code=200, response_model=list[UserOutput] )
async def get_all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.query(UserModel).all()
    if users is None:
        raise HTTPException(status_code=404, detail="Users not found")
    return users

@user_router.get('/country_name/{country_name}', status_code=200, response_model=list[UserOutputCountry])
async def get_user_by_country(country_name: str, db: Annotated[Session, Depends(get_db)]):
    if country_name is None:
        raise HTTPException(status_code=404, detail="Country not found")
    country_user = country_name.upper()
    country = db.query(CountryModel).filter(CountryModel.country_name == country_user).first()
    return db.query(UserModel).filter(UserModel.usr_country_id == country.country_id).all()

@user_router.get('/language_name/{language_name}', status_code=200, response_model=list[UserOutputLanguage])
async def get_user_by_country(language_name: str, db: Annotated[Session, Depends(get_db)]):
    if language_name is None:
        raise HTTPException(status_code=404, detail="Language not found")
    language_user = language_name.upper()
    language = db.query(LanguageModel).filter(LanguageModel.language_name == language_user).first()
    return db.query(UserModel).filter(UserModel.usr_language_id == language.language_id).all()



@user_router.put('/logic_delete/{user_email}', status_code=200)
async def logic_delete_user(user_email: str, db: Annotated[Session, Depends(get_db)]):
    if user_email is None:
        raise HTTPException(status_code=404, detail="User not found")
    user = db.query(UserModel).filter(UserModel.usr_email == user_email).first()
    user.usr_is_active = False
    db.commit()
    return "El usuario ha sido eliminado logicamente"



