import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Annotated
from urllib.parse import urlencode

from passlib.context import CryptContext
from schemas.auth import Token
from schemas.auth.email import Email

'''' HASHING PASSWORD WITH BCRYPT '''
# Create a global object of CryptContext
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto" )

# Create encrypted hash password
def get_password_hash(password):
  return bcrypt_context.hash(password)

#Verify user login password (plain_password) with hash password in the db
def verify_password(plain_password, hash_password):
  return bcrypt_context.verify(plain_password, hash_password)
''' END HASHING PASSWORD WITH BCRYPT'''



''' SEND EMAIL '''
def send_email(usr_email: str, token: Token):
  
  verification_url = f"http://localhost:8000/auth/verify?{urlencode({'token': token})}"
  
  body = f"""
    <html>
    <body>
        <p>Hola,</p>
        <p>Gracias por registrarte. Haz clic en el siguiente enlace para verificar tu cuenta:</p>
        <p><a href="{verification_url}">{verification_url}</a></p>
    </body>
    </html>
    """
    
  email = Email(
    sender_email="miemail",
    sender_password="micontraseña",
    receiver_email=usr_email,
    subject="¡Hola!",
    message=body
  )
  
  msg = MIMEMultipart()
  msg["From"] = email.sender_email
  msg["To"] = email.receiver_email
  msg["Subject"] = email.subject
  
  with smtplib.SMTP("smtp-mail.outlook.com", 587) as server:
    server.starttls()
    server.login(email.sender_email, email.sender_password.encode('utf-8'))
    server.send_message(msg)

''' END SEND EMAIL'''
  
  









