from sqlalchemy.orm import Session
from sqlalchemy import and_
from datetime import date
import models, shemas


def get_smartmodule_by_identification_key(db: Session, identification_key: str):
    return db.query(models.SmartModule).filter(models.SmartModule.identification == identification_key).first()


def change_smartmodule_user_status(db: Session, identification_key: str, user_id: int, status: int):
    db_smartmodule = get_smartmodule_by_identification_key(db, identification_key)
    db_smartmodule.last_user_id = user_id
    db_smartmodule.session_status = status
    db.add(db_smartmodule)
    db.commit()
    db.refresh(db_smartmodule)
    return db_smartmodule




def update_calories(db: Session, user_id: int, calories: int):
    db_workout = get_user_workout(db, user_id)[-1]
    db_workout.calories += calories
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    return db_workout
def update_pull_ups_for_workout(db: Session, user_id: int, pull_ups: shemas.PublicPullUps):
    db_workout = get_user_workout(db, user_id)[-1]
    db_workout.count_of_pull_up_great += pull_ups.count_of_pull_up_great
    db_workout.count_of_pull_up_medium += pull_ups.count_of_pull_up_medium
    db_workout.count_of_pull_up_bad += pull_ups.count_of_pull_up_bad
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    return db_workout


def get_user_goals(db: Session, user_id: int):
    return db.query(models.Goals).filter(models.Goals.owner_id == user_id).all()


def create_user_goals(db: Session, goals: shemas.GoalsCreate):
    db_goals = models.Goals(**goals.dict())
    db.add(db_goals)
    db.commit()
    db.refresh(db_goals)
    return db_goals


def create_smart_module(db: Session, smart_module: shemas.SmartModule):
    db_smart = models.SmartModule(**smart_module.dict())
    db.add(db_smart)
    db.commit()
    db.refresh(db_smart)
    return db_smart


def get_user_workout(db: Session, user_id: int, data_begin: date = None, data_end: date = None):
    if data_begin and data_end:
        return db.query(models.Workout).filter(models.Workout.owner_id == user_id).filter(
            and_(models.Workout.data >= data_begin, models.Workout.data <= data_end)).all()
    elif data_begin:
        return db.query(models.Workout).filter(models.Workout.owner_id == user_id).filter(
            models.Workout.data >= data_begin).all()
    else:
        return db.query(models.Workout).filter(models.Workout.owner_id == user_id).all()


def create_user_workout(db: Session, workout: shemas.Workout):
    db_workout = models.Workout(**workout.dict())
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    return db_workout


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


#
def create_user(db: Session, user: shemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
