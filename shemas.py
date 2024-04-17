from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import date


class UserBase(BaseModel):
    email: EmailStr


class UserOut(UserBase):
    firstname: str
    lastname: str
    user_id: int
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


# class GoalsCreate(BaseModel):
#     goals_for_week: int
#     goals_for_month: int
#     goals_for_year: int
#     owner_id: int

# class Goals(GoalsCreate):
#     pass

class SmartModule(BaseModel):
    identification: str
    session_status: int
    user_id: int
class PublicPullUps(BaseModel):
    identification: str
    count_of_pull_up_great: int
    # count_of_pull_up_medium: int
    # count_of_pull_up_bad: int

class Workout(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    firstname: str
    lastname: str
    patronymic: str
    sex_id: int
    old: int
    key: str
    identification_key: str
    # count_of_pull_up_medium: int
    # count_of_pull_up_bad: int
    # calories: int

    user_id: int

class WorkoutOut(BaseModel):
    firstname: str
    lastname: str
    patronymic: str
    name: str
    old: int
    count_of_pull_up_great: int
class CreateWorkout(BaseModel):
    data: date
    count_of_pull_up_great: int
    athlete_id: int
    user_id: int

class Athlete(BaseModel):

    firstname: str
    lastname: str
    patronymic: str
    sex_id: int
    old: int
    key: str

