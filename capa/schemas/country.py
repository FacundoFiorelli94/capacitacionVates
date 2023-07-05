from pydantic import BaseModel


class CountryBase(BaseModel):
    country_id: int


class CountryOutput(CountryBase):
    country_name: str

    class Config:
        orm_mode = True