from db import create_tables
from fastapi import FastAPI
from routes.auth import auth_router
from routes.user import user_router
from routes.country import country_router
from routes.language import language_router

app = FastAPI()

create_tables()

app.include_router( auth_router )
app.include_router( user_router )
app.include_router( country_router )
app.include_router( language_router )

@app.get('/')
def home():
  return 'Hello'








