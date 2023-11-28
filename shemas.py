from pydantic import BaseModel, EmailStr
from datetime import date


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

class UserCreate(UserBase):
    firstname: str
    lastname: str
    weight: int
    height: int
    hashed_password: str


class UserIn(UserBase):
    password: str


class GoalsCreate(BaseModel):
    goals_for_week: int
    goals_for_month: int
    goals_for_year: int
    owner_id: int

class Goals(GoalsCreate):
    pass

class Workout(BaseModel):
    data: date
    count_of_pull_up_great: int
    count_of_pull_up_medium: int
    count_of_pull_up_bad: int
    calories: int
    owner_id: int

