from sqlalchemy import Column, ForeignKey, Integer, Date
from sqlalchemy.orm import relationship
from models.users import User
from db import Base

class Workout(Base):
    __tablename__ = "workout"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(Date, index=True)
    count_of_pull_up_great = Column(Integer, index=True)

    athlete_id = Column(Integer, ForeignKey("athletes.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    athlete = relationship("Athlete", back_populates="workout")
    owner = relationship("User", back_populates="workout")


