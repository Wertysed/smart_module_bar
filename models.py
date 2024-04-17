from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from db import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    hashed_password = Column(String)

    workout = relationship("Workout", back_populates="owner")

class Athlete(Base):
    __tablename__ = "athletes"

    athlete_id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    patronymic = Column(String)
    sex_id = Column(Integer, ForeignKey("sex.sex_id"))
    old = Column(Integer)
    key = Column(String)

    sex = relationship("Sex", back_populates="athlete")
    workout = relationship("Workout", back_populates="athlete")

class Sex(Base):
    __tablename__ = "sex"

    sex_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    athlete = relationship("Athlete", back_populates="sex")


class Workout(Base):
    __tablename__ = "workout"

    workout_id = Column(Integer, primary_key=True, index=True)
    # title = Column(String, index=True)
    data = Column(Date, index=True)
    # description = Column(String, index=True)
    count_of_pull_up_great = Column(Integer, index=True)
    # count_of_pull_up_medium = Column(Integer, index=True)
    # count_of_pull_up_bad = Column(Integer, index=True)
    # calories = Column(Integer, index=True)

    athlete_id = Column(Integer, ForeignKey("athletes.athlete_id"))
    user_id = Column(Integer, ForeignKey("users.user_id"))

    athlete = relationship("Athlete", back_populates="workout")
    owner = relationship("User", back_populates="workout")


# class Goals(Base):
    # __tablename__ = 'goals'
    #
    # id = Column(Integer, primary_key=True, index=True)
    # goals_for_week = Column(Integer, index=True)
    # goals_for_month = Column(Integer, index=True)
    # goals_for_year = Column(Integer, index=True)
    # owner_id = Column(Integer, ForeignKey("users.id"))
    #
    # owner = relationship("User", back_populates="goals")


class SmartModule(Base):
    __tablename__ = 'smart_module'

    smart_module_id = Column(Integer, primary_key=True, index=True)
    identification = Column(String, index=True)
    session_status = Column(Integer, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))

