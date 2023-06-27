from pydantic import BaseModel


class UserOutput(BaseModel):
    usr_id: int
    usr_email: str
    usr_country_id: int
    usr_language_id: int

    class Config:
      orm_mode = True
    

class UserBase(UserOutput):
  usr_password: str
  usr_address: str
  usr_zip: int
  usr_phone:int
  usr_enabled: bool = False
  usr_is_active: bool = True

  class Config:
    orm_mode = True

