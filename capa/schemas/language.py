from pydantic import BaseModel, Field


class LanguageCreate(BaseModel):
  language_name: str  = Field(regex=r"^[a-zA-Z]+(?:\\s[a-zA-Z]+)*$", max_length=20)


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