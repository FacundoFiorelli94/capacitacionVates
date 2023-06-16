from pydantic import BaseModel
from  models.models import CountryModel, UserModel, LanguageModel
#discutir

class UserOutput(BaseModel):
    email: str
    name: str

    is_enabled: bool
    
    @property
    def country_name(self):
        return CountryModel.get(id=self.country_id).name
    def language_name(self):
        return LanguageModel.get(id=self.language_id).name


class UserCreate(UserOutput):
    password: str


class User(UserCreate):
    id: int
    items: list[Item] = []

    class Config:
        orm_mode = True

class CountryOutout(BaseModel):
    name: str