from pydantic import BaseModel


class LanguageBase(BaseModel):
    language_id: int


class LanguageOutput(LanguageBase):
    language_name: str

    class Config:
        orm_mode = True