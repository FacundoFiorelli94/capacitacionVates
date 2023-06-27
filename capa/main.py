from db import create_tables
<<<<<<< HEAD
from fastapi import FastAPI
from routers.auth import auth_router
from routers.user import user_router
from routers.country import country_router
from routers.language import language_router
=======
from routes.auth import auth_router
>>>>>>> main

app = FastAPI()

create_tables()

app.include_router( auth_router )
app.include_router( user_router )
app.include_router( country_router )
app.include_router( language_router )

@app.get('/')
def home():
  return 'Hello'








