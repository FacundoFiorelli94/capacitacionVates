from db import Base
from models.country import CountryModel
from models.language import LanguageModel
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class UserModel(Base):
  __tablename__ = 'users'
  usr_id = Column(Integer, primary_key=True, index=True)
  usr_email = Column(String, unique=True, index=True)
  usr_password = Column(String)
  usr_address = Column(String)
  usr_zip = Column(Integer)
  usr_phone = Column(String)
  usr_country_id = Column(Integer, ForeignKey('country.country_id'))
  usr_language_id = Column(Integer, ForeignKey('language.language_id'))
  usr_enabled = Column(Boolean, default=False)
  usr_is_active = Column(Boolean, default=True)

  country = relationship("CountryModel", back_populates="user")
  language = relationship("LanguageModel", back_populates="user")
