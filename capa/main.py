from db import create_tables
from fastapi import FastAPI
from routers.auth import auth_router
from routers.user import user_router

app = FastAPI()

create_tables()

app.include_router( auth_router )
app.include_router( user_router )

@app.get('/')
def home():
  return 'Hello'








