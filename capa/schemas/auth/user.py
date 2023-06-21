from models.country import CountryModel
from models.language import LanguageModel
from pydantic import BaseModel, EmailStr


###discutir (abi)
class UserOutput(BaseModel):
    usr_email: EmailStr
    # usr_name: str

    # usr_enabled: bool
    
    @property
    def country_name(self):
        return CountryModel.get(id=self.country_id).name
    def language_name(self):
        return LanguageModel.get(id=self.language_id).name


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


