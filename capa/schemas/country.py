from pydantic import BaseModel, Field

class CountryCreate(BaseModel):
  country_name: str = Field(regex=r'^(?! )[\w\s]+(?<! )$', max_length=20)

class Country(CountryCreate):
  country_id: int

  class Config:
    orm_mode = True


class UserOutputCountry(BaseModel):
  usr_email: str
  usr_country_id: int

  class Config:
    orm_mode = True
    

class UserBaseCountry(UserOutputCountry):
  usr_id: int
  usr_password: str
  usr_address: str
  usr_zip: int
  usr_phone:int
  usr_enabled: bool = False
  usr_language_id: int
  usr_is_active: bool = True

  class Config:
    orm_mode = True