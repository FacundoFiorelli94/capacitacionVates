from db import Base
from sqlalchemy import Column, Integer, String


class LanguageModel(Base):
  __tablename__ = 'language'

  language_id = Column(Integer, primary_key=True, index=True)
  language_name = Column(Integer, unique=True)
