from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    hashed_password = Column(String)
    height = Column(Integer, index=True)
    weight = Column(Integer, index=True)

    workout = relationship("Workout", back_populates="owner")
    goals = relationship("Goals", back_populates="owner")

class Workout(Base):
    __tablename__ = "workout"

    id = Column(Integer, primary_key=True, index=True)
    #title = Column(String, index=True)
    data = Column(Date, index=True)
    #description = Column(String, index=True)
    count_of_pull_up_great = Column(Integer, index=True)
    count_of_pull_up_medium = Column(Integer, index=True)
    count_of_pull_up_bad = Column(Integer, index=True)
    calories = Column(Integer, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="workout")

class Goals(Base):
    __tablename__ = 'goals'

    id = Column(Integer, primary_key=True, index=True)
    goals_for_week = Column(Integer, index=True)
    goals_for_month = Column(Integer, index=True)
    goals_for_year = Column(Integer, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="goals")