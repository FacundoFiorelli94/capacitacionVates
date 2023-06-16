from pydantic import BaseModel, EmailStr


class UserOutPut(BaseModel):
    usr_email: EmailStr
    usr_enabled: bool = False
    usr_country_name: str
    usr_language_name: str
    usr_role: str = 'user'



class UserLoginRequest(BaseModel):
    usr_email: EmailStr
    usr_password: str


class CreateUserRequest(UserLoginRequest):    
  usr_address: str
  usr_zip: int
  usr_phone: str
  usr_country_name: str
  usr_language_name: str
  usr_enabled: bool = False
  
  class config:
    orm_mode = True





