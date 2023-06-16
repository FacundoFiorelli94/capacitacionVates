from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db import Base


class UserModel(Base):
    tablename = 'user'

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String(50), unique=True)
    hashed_password = Column(String)
    is_enabled = Column(Boolean)
    country_id = Column(Integer, ForeignKey('country.country_id'))
    language_id = Column(Integer, ForeignKey('language.language_id'))
    adress = Column(String)
    phone = Column(Integer)
    zip = Column(Integer)
    name = Column(String, unique=True, index=True)
   

class CountryModel(Base):
    tablename = 'country'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Integer, unique=True)


class LanguageModel(Base):
    tablename = 'language'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Integer, unique=True)

