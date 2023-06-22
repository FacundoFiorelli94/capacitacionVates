from datetime import timedelta

from db import get_db
from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic.typing import Annotated
from schemas.auth.Token import Token
from schemas.auth.user import CreateUserRequest
from services.auth import (authenticate_user, create_access_token, create_user,
                           get_current_user)
from sqlalchemy.orm import Session

auth_router = APIRouter(
  prefix='/auth',
  tags=['Auth'],
)

db_dependency = Annotated[ Session, Depends(get_db)]
user_dependency = Annotated[ dict, Depends(get_current_user)]
oauhh2_bearer = OAuth2PasswordBearer(tokenUrl='/auth/login')


@auth_router.post('/register', response_model=CreateUserRequest, response_model_exclude=['usr_password'], status_code=status.HTTP_201_CREATED)
async def register(user: CreateUserRequest, db: db_dependency):
  await create_user(db, user) 
  return user

@auth_router.get('/verify_email/{token}', status_code=status.HTTP_202_ACCEPTED)
def verify_email(token: str):
  pass

@auth_router.post('/login', response_model=Token, status_code=status.HTTP_200_OK)
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency, response: Response):
  user = authenticate_user(form_data.username, form_data.password, db  )
  
  token = create_access_token(user.usr_email, user.usr_id, timedelta(minutes=15))
  response.set_cookie(key="token", value=token)
  return {'access_token': token, 'token_type': 'bearer'}

@auth_router.post('/logout')
def logout():
  return 'OKk'

