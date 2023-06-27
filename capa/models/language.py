from db import Base
from models.user import *
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class LanguageModel(Base):
   __tablename__ = 'language'

   language_id = Column(Integer, primary_key=True, index=True)
   language_name = Column(String, unique=True)

   user = relationship("UserModel", back_populates="language")