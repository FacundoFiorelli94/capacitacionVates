from fastapi import FastAPI
from db import create_tables
from routes.auth import auth_router

app = FastAPI()

create_tables()

app.include_router( auth_router )

@app.get('/')
def home():
  return 'Hello'








