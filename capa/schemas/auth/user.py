from pydantic import BaseModel, EmailStr, Field


class UserLogin(BaseModel):
  usr_email: EmailStr
  usr_password: str

class UserCreate(UserLogin):
  usr_address: str = Field(regex=r"^(?!.*\s\s)[^\s].*[^\s]$")
  usr_zip: int
  usr_phone: str = Field(regex="^\+?\d{1,3}[-.\s]?\(?\d{1,3}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}$")
  usr_country_id: int
  usr_language_id: int


class User(UserCreate):
  usr_id: int
  usr_enabled: bool = False
  usr_is_active: bool = True
  
  class Config:
    orm_mode = True
  

