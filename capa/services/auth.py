from datetime import timedelta, datetime
from fastapi import HTTPException, status, Depends
from schemas.auth.user import CreateUserRequest
from sqlalchemy.orm import Session
from models.user import UserModel
from utils.utils import get_password_hash, verify_password
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from pydantic.typing import Annotated
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from typing import List
from pydantic import EmailStr, BaseModel


class EmailSchema(BaseModel):
    email: List[EmailStr]


conf = ConnectionConfig(
    MAIL_USERNAME="pilcapa2023@gmail.com",
    MAIL_PASSWORD="ofmmifkfjjtwqyfq",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    MAIL_FROM="pilcapa2023@gmail.com",
)


async def create_user(db: Session, user: CreateUserRequest):
    usr_email = (
        db.query(UserModel).filter(UserModel.usr_email == user.usr_email).first()
    )

    if usr_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email registrado"
        )

    hashed_password = get_password_hash(user.usr_password)

    user.usr_password = hashed_password
    db_user = UserModel(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    token = create_access_token(
        db_user.usr_email, db_user.usr_id, timedelta(minutes=15)
    )
    template = f"""
        <html>
        <body>
         
 
        <p>Hi !!!
        <br>token: {token}</p>
 
 
        </body>
        </html>
        """
    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=[user.usr_email],  # List of recipients, as many as you can pass
        body=template,
        subtype="html",
    )
    fm = FastMail(conf)
    await fm.send_message(message)
    # send_email(user.usr_email, token)


def authenticate_user(
    usr_email: str,
    usr_password: str,
    db: Session,
):
    user = db.query(UserModel).filter(UserModel.usr_email == usr_email).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario o contraseña incorrecto",
        )
    if not verify_password(usr_password, user.usr_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario o contraseña incorrecto",
        )

    return user


""" CREATE TOKEN """
SECRET_KEY = "MiSuperSecretKey"
ALGORITHM = "HS256"


def create_access_token(usr_email: str, usr_id, expires_delta: timedelta):
    encode = {"email": usr_email, "id": usr_id}
    expires_delta = datetime.utcnow() + expires_delta
    encode.update({"exp": expires_delta})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


""" END CREATE TOKEN"""


"""GET CURRENT USER"""
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        usr_email = payload.get("email")
        usr_id = payload.get("id")
        if usr_email is None or usr_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Usuario no autorizado gcu",
            )
        return {"usr_email": usr_email, "usr_id": usr_id}
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario no autorizado gcu jwtError",
        )


"""END GET CURRENT USER"""
