from pydantic import BaseModel


class LanguageCreate(BaseModel):
    language_name: str


class Language(LanguageCreate):
    language_id: int

    class Config:
        orm_mode = True

class UserOutputLanguage(BaseModel):
    usr_email: str
    usr_language_id: int

    class Config:
        orm_mode = True
    

class UserBaseLanguage(UserOutputLanguage):
  usr_id: int
  usr_password: str
  usr_address: str
  usr_zip: int
  usr_phone:int
  usr_enabled: bool = False
  usr_country_id: int
  usr_is_active: bool = True

  class Config:
    orm_mode = True