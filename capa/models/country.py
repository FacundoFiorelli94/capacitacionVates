from db import Base
from models.user import *
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class CountryModel(Base):
   __tablename__ = 'country'

   country_id = Column(Integer, primary_key=True, index=True)
   country_name = Column(String, unique=True)

   user = relationship("UserModel", back_populates="country")