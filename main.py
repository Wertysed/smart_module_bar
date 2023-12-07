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

@app.get("/identification_module")
async def identification_module(identification_key: str, db: Session = Depends(get_db)):
    return services.get_smartmodule(db, identification_key)



@app.post("/registration", response_model=shemas.UserOut)
async def registration(user: Annotated[shemas.UserReg, Body()] = None, db: Session = Depends(get_db)):
    user = services.registration(user, db)
    return user


@app.post("/create_smart_module", response_model=shemas.SmartModule)
async def create_smart_module(smart_module: Annotated[shemas.SmartModule, Body()] = None, db: Session = Depends(get_db)):
    new_smart_module = services.create_smart_module(db, smart_module)
    return new_smart_module

@app.post("/start_workout")
async def start_workout(user_id: int, identification_key: str, db: Session = Depends(get_db)):
    workout_new = shemas.Workout(data=date.today(), count_of_pull_up_great=0, count_of_pull_up_medium=0, count_of_pull_up_bad=0, calories=0, owner_id=user_id)
    workout = services.create_user_workout(db, workout_new)
    new_status = services.change_smartmodule_user_status(db, identification_key, user_id, status=1)
    return {"message": "workout starts!"}

@app.post("/end_workout")
async def end_workout(user_id: int, identification_key: str, db: Session = Depends(get_db)):
    new_status = services.change_smartmodule_user_status(db, identification_key, user_id, status=0)
    return {"message": "workout ends!"}
@app.post("/public_pull_ups")
async def public_pull_ups(data: Annotated[shemas.PublicPullUps, Body()] = None, db: Session = Depends(get_db)):
    status = services.public_pull_ups(db, data)
    if status:
        return {"message": "pull ups counted"}
    else:
        return {"message": "pull ups doesnt counted"
                           ""}