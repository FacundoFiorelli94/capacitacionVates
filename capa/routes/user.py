from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from db import get_db
from models.user import UserModel
from schemas.user_crud import UserOutput
from sqlalchemy.orm import Session

user_router = APIRouter(
  prefix='/user',
  tags=['user'],
)


@user_router.get('/get_users', status_code=200, response_model=list[UserOutput] )
async def get_all_users(db: Annotated[Session, Depends(get_db)], country_id: int = None, language_id: int = None):

  query = db.query(UserModel)
  
  if country_id:
    query = query.filter_by( usr_country_id=country_id)

  if language_id:
    query = query.filter_by(usr_language_id=language_id)

  users = query.all()
  return users



#! DEPRECATED -----------------------------
# @user_router.get('/country_name/{country_name}', status_code=200, response_model=list[UserOutputCountry], deprecated=True)
# async def get_user_by_country(country_name: str, db: Annotated[Session, Depends(get_db)]):
#     if country_name is None:
#         raise HTTPException(status_code=404, detail="Country not found")
#     country_user = country_name.upper()
#     country = db.query(CountryModel).filter(CountryModel.country_name == country_user).first()
#     return db.query(UserModel).filter(UserModel.usr_country_id == country.country_id).all()

# @user_router.get('/language_name/{language_name}', status_code=200, response_model=list[UserOutputLanguage],deprecated=True)
# async def get_user_by_country(language_name: str, db: Annotated[Session, Depends(get_db)]):
#     if language_name is None:
#         raise HTTPException(status_code=404, detail="Language not found")
#     language_user = language_name.upper()
#     language = db.query(LanguageModel).filter(LanguageModel.language_name == language_user).first()
#     return db.query(UserModel).filter(UserModel.usr_language_id == language.language_id).all()
#! DEPRECATED -----------------------------


@user_router.put('/logic_delete/{user_email}', status_code=200)
async def logic_delete_user(user_email: str, db: Annotated[Session, Depends(get_db)]):
    if user_email is None:
        raise HTTPException(status_code=404, detail="User not found")
    user = db.query(UserModel).filter_by(usr_email= user_email).first()
    user.usr_is_active = False
    db.commit()
    return "El usuario ha sido eliminado logicamente"




