from pydantic import BaseModel, EmailStr, Field

#! No hace falta la clase UserBase porque no se usa en ningun lado 
#! Ya que este esquema no se usa en la ruta de creacion de usuario ni de login
# class UserBase(BaseModel):
#   usr_password: str

class UserOutput(BaseModel):
  usr_id: int
  usr_email: EmailStr
  usr_country_id: int
  usr_language_id: int
  usr_address: str
  usr_zip: int
  usr_phone: str = Field(regex="^\+?\d{1,3}[-.\s]?\(?\d{1,3}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}$")
  usr_enabled: bool = False
  usr_is_active: bool = True
    

  class Config:
    orm_mode = True




