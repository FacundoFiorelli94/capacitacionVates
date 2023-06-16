from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db import Base


class UserModel(Base):
  __tablename__ = 'users'
  usr_id = Column(Integer, primary_key=True, index=True)
  usr_email = Column(String, unique=True, index=True)
  usr_password = Column(String)
  usr_address = Column(String)
  usr_zip = Column(Integer)
  usr_phone = Column(String)
  usr_country_id = Column(Integer, ForeignKey('CountrysModel.country_id'))
  usr_language_id = Column(Integer, ForeignKey('LanguagesModel.language_id'))
  usr_enabled = Column(Boolean, default=False)

class CountrysModel(Base):
  __tablename__ = 'country'

  country_id = Column(Integer, primary_key=True, index=True)
  country_name = Column(Integer, unique=True)


class LanguagesModel(Base):
  __tablename__ = 'language'

  languages_id = Column(Integer, primary_key=True, index=True)
  languages_name = Column(Integer, unique=True)

