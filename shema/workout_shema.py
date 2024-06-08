from pydantic import BaseModel, ConfigDict
from datetime import date
from shema.athlete_shema import Athlete


class Workout(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    firstname: str
    lastname: str
    patronymic: str
    sex_id: int
    old: int
    key: str
    identification_key: str
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
class PublicPullUps(BaseModel):
    identification: str
    count_of_pull_up_great: int

class WorkNew(BaseModel):
    data: date
    count_of_pull_up_great: int

    athlete: "Athlete"
