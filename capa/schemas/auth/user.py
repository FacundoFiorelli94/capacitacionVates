
from pydantic import BaseModel, EmailStr


###discutir (abi)
class UserOutput(BaseModel):
    usr_email: EmailStr
    class config:
        orm_mode = True


class UserLoginRequest(UserOutput):
    # usr_email: EmailStr
    usr_password: str

class CreateUserRequest(UserLoginRequest):    
  usr_address: str
  usr_zip: int
  usr_phone: str
  usr_country_id: int
  usr_language_id: int
  usr_enabled: bool = False  
  
  class config:
    orm_mode = True


