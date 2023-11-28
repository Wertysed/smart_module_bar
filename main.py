from fastapi import FastAPI, Body, Depends, Query
from typing import Annotated, Any
from sqlalchemy.orm import Session
import shemas, models, crud, services
from db import SessionLocal, engine
from passlib.context import CryptContext
from datetime import date
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/create_workout", response_model=shemas.Workout)
async def create_workout(workout: Annotated[shemas.Workout, Body()] = None, db: Session = Depends(get_db)):
    workout = services.create_user_workout(db, workout)
    return workout


@app.get("/workouts/{owner_id}", response_model=list[shemas.Workout])
async def get_user_workouts(owner_id: int, db: Session = Depends(get_db), data_begin: Annotated[date, Query()] = None,
                            data_end: Annotated[date, Query()] = None):
    workouts = services.get_user_workout(db, owner_id, data_begin, data_end)
    return workouts


@app.post("/create_goals", response_model=shemas.Goals)
async def create_goals(goals: Annotated[shemas.GoalsCreate, Body()] = None, db: Session = Depends(get_db)):
    goals = services.create_user_goals(db, goals)
    return goals


@app.get("/goals/{owner_id}", response_model=list[shemas.Goals])
async def get_user_goals(owner_id: int, db: Session = Depends(get_db)):
    goals = services.get_user_goals(db, owner_id)
    return goals


@app.post("/login", response_model=shemas.UserOut)
async def login(user: Annotated[shemas.UserIn, Body()] = None, db: Session = Depends(get_db)):
    user = services.login(user, db)
    return user


@app.post("/registration", response_model=shemas.UserOut)
async def registration(user: Annotated[shemas.UserReg, Body()] = None, db: Session = Depends(get_db)):
    user = services.registration(user, db)
    return user
