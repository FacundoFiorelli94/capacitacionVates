from pydantic import BaseModel, EmailStr, Field


class UserOutput(BaseModel):
    usr_email: EmailStr
    usr_address: str = Field(regex="^[a-zA-Z0-9\s\-\#\.\,]+$")
    usr_zip: int
    usr_phone: str = Field(regex="^\+?\d{1,3}[-.\s]?\(?\d{1,3}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}$")
    usr_country_id: int
    usr_language_id: int
    usr_enabled: bool = False
    usr_is_active: bool = True


class UserCreate(UserOutput):
    usr_password: str = Field(regex="^[a-zA-Z0-9]+(?:\\s[a-zA-Z0-9]+)*$", max_length=30, min_length=8)  # permite letras y numeros, permite espacios entre las palabras pero no al principio o al final de la oracion
    # usr_password: str = Field(regex='^(?=.*[A-Z])(?=.*[!@#$%^&*()-=_+[\];:"|,.<>/?])[a-zA-Z0-9]+(?:\s[a-zA-Z0-9]+)*$', max_length=30, min_length=8) #permite letras y numeros, permite espacios entre las palabras pero no al principio o al final de la oracion, y ademas exige una letra mayuscula y un caracter especial (no lo probe)


class User(UserCreate):
    usr_id: int

    class config:
        orm_mode = True
