from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr


class UserOut(UserBase):
    firstname: str
    lastname: str

class UserReg(UserBase):
    firstname: str
    lastname: str
    weight: int
    height: int

    password: str
    password_again: str

class UserInDb(UserBase):
    firstname: str
    lastname: str
    weight: int
    height: int
    hashed_password: str


class UserIn(UserBase):
    password: str