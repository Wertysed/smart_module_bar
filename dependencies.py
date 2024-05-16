from fastapi import Depends
from sqlalchemy.orm import Session
from repositories.athlete_repository import AthleteRepository
from db import SessionLocal
from repositories.smart_module_repository import SmartModuleRepository
from services.smart_module_service import SmartModuleService
from repositories.user_repository import UserRepository
from services.user_service import UserService
from repositories.workout_repository import WorkoutRepository
from services.workout_service import WorkoutService

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



def user_service(db: Session = Depends(get_db)):
    return UserService(UserRepository(db))

def workout_service(db: Session = Depends(get_db)):
    return WorkoutService(WorkoutRepository(db), AthleteRepository(db), SmartModuleRepository(db))

def smart_module_service(db: Session = Depends(get_db)):
    return SmartModuleService(SmartModuleRepository(db))
