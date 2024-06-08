from pydantic import BaseModel
from shema.sex_shema import Sex

class Athlete(BaseModel):

    firstname: str
    lastname: str
    patronymic: str
    sex: "Sex"
    old: int
    key: str
class AthleteSh(BaseModel):

    firstname: str
    lastname: str
    patronymic: str
    sex_id: int 
    old: int
    key: str

