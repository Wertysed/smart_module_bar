from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from models.sex import Sex
from models.workout import Workout
from db import Base

class Athlete(Base):
    __tablename__ = "athletes"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    patronymic = Column(String)
    sex_id = Column(Integer, ForeignKey("sex.id"))
    old = Column(Integer)
    key = Column(String)

    sex = relationship("Sex", back_populates="athlete")
    workout = relationship("Workout", back_populates="athlete")


