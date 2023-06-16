from pydantic  import BaseModel



class Email(BaseModel):
  sender_email: str
  sender_password: str
  receiver_email: str
  subject: str
  message: str




