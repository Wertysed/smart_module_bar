from pydantic import BaseModel, EmailStr
from datetime import date


class UserBase(BaseModel):
    email: EmailStr


class UserOut(UserBase):
    firstname: str
    lastname: str
    id: int
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

class SmartModule(BaseModel):
    identification: str
    session_status: int
    last_user_id: int
class PublicPullUps(BaseModel):
    identification: str
    count_of_pull_up_great: int
    count_of_pull_up_medium: int
    count_of_pull_up_bad: int

class Workout(BaseModel):
    data: date
    count_of_pull_up_great: int
    count_of_pull_up_medium: int
    count_of_pull_up_bad: int
    calories: int
    owner_id: int

