from db import create_tables
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.auth import auth_router
from routes.user import user_router
from routes.country import country_router
from routes.language import language_router

app = FastAPI()
origins = [

    "http://localhost:3000",

]

 

# Agregar el middleware CORS

app.add_middleware(

    CORSMiddleware,

    allow_origins=origins,

    allow_credentials=True,

    allow_methods=["GET", "POST", "PUT", "DELETE"],

    allow_headers=["*"],

)
create_tables()

app.include_router( auth_router )
app.include_router( user_router )
app.include_router( country_router )
app.include_router( language_router )

@app.get('/')
def home():
  return 'Hello'








