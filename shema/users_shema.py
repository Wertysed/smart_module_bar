from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr


class UserOut(UserBase):
    firstname: str
    lastname: str
    id: int
class UserReg(UserBase):
    firstname: str
    lastname: str

    password: str
    password_again: str

class UserCreate(UserBase):
    firstname: str
    lastname: str
    hashed_password: str


class UserIn(UserBase):
    password: str



