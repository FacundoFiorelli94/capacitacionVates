from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


#! CAMBIAR POR LOS DATOS DE SU BASE DE DATOS

#SQLALCHEMY_DATABASE_URL = "postgresql://USUARIO:CONTRASEÑA@localhost:5432/capa"
SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

engine = create_engine( SQLALCHEMY_DATABASE_URL )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def create_tables():
  Base.metadata.create_all(bind=engine)
    
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

