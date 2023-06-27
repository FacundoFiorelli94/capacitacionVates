from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv.main import load_dotenv
import os


load_dotenv()
user_postgres=os.environ['USER_POSTGRES']
pass_postgres=os.environ['PASS_POSTGRES']


SQLALCHEMY_DATABASE_URL = f"postgresql://{user_postgres}:{pass_postgres}@localhost:5432/capa"

engine = create_engine( SQLALCHEMY_DATABASE_URL )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

meta = MetaData();

def create_tables():
  Base.metadata.create_all(bind=engine)
    
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()
