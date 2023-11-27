from fastapi import FastAPI, Body
from typing import Annotated, Any
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserBase(BaseModel):
    email: EmailStr


class UserOut(UserBase):
    first_name: str


class UserReg(UserBase):
    first_name: str
    last_name: str
    password: str


class UserInDb(UserBase):
    hash_password: str


class UserIn(UserBase):
    password: str


@app.post("/login", response_model=UserOut)
async def test(user: Annotated[UserIn, Body()] = None):
    user_out = UserOut(**user.dict(), first_name="kaban")
    return user_out


@app.post("/registration", response_model=UserOut)
async def test(user: Annotated[UserReg, Body()] = None):
    return user

