import crud
from sqlalchemy.orm import Session
import shemas
from passlib.context import CryptContext
from datetime import date
import segno


qrcode = segno.make_qr("Hello, World")
qrcode.save("basic_qrcode.png")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_smartmodule(db: Session,identification_key:str):
    return crud.get_smartmodule_by_identification_key(db, identification_key)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_user_goals(db: Session, goals: shemas.GoalsCreate):
    goals = crud.create_user_goals(db, goals)
    return goals


def get_user_goals(db: Session, user_id: int):
    goals = crud.get_user_goals(db, user_id)
    return goals


def get_user_workout(db: Session, user_id: int, data_begin: date = None, data_end: date = None):
    workout = crud.get_user_workout(db, user_id, data_begin, data_end)
    return workout



def create_user_workout(db: Session, workout: shemas.Workout):
    workout = crud.create_user_workout(db, workout)
    return workout


def registration(user: shemas.UserReg, db: Session):
    user = crud.create_user(db, shemas.UserCreate(**user.dict(), hashed_password=get_password_hash(user.password)))
    return user


def login(user: shemas.UserIn, db: Session):
    user_db = crud.get_user_by_email(db, user.email)
    if user_db:
        if verify_password(user.password, user_db.hashed_password):
            return user_db
    return False
