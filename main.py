from fastapi import FastAPI, Body, Depends
from typing import Annotated
from dependencies import smart_module_service, user_service, workout_service
import shemas, models
from db import SessionLocal, engine
from passlib.context import CryptContext
from fastapi.middleware.cors import CORSMiddleware
from services.smart_module_service import SmartModuleService
from services.user_service import UserService
from services.workout_service import WorkoutService

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/create_workout" )
async def create_workout(workout: Annotated[shemas.Workout, Body()], workout_service: Annotated[WorkoutService, Depends(workout_service)]):
    return workout_service.create(workout) 


@app.get("/workouts/{owner_id}", response_model=list[shemas.WorkNew])
async def get_user_workouts(owner_id: int, workout_service: Annotated[WorkoutService, Depends(workout_service)]):
    return workout_service.read_by_options({"user_id": owner_id})

@app.get("/workout/{id}", response_model=shemas.WorkNew)
async def get_workout_by_id(id: int, workout_service: Annotated[WorkoutService, Depends(workout_service)]):
    return workout_service.read_by_id(id) 

@app.get("/user/{id}", response_model=shemas.UserOut)
async def get_user_by_id(id: int, user_service: Annotated[UserService, Depends(user_service)]):
    return user_service.read_by_id(id) 


@app.post("/login", response_model=shemas.UserOut)
async def login(user: Annotated[shemas.UserIn, Body()], user_service: Annotated[UserService, Depends(user_service)]):
    return user_service.sign_in(user) 

@app.get("/identification_module")
async def identification_module(identification_key: str, smart_module_service: Annotated[SmartModuleService, Depends(smart_module_service)]):
    return smart_module_service.read_by_options({"identification": identification_key}) 



@app.post("/registration", response_model=shemas.UserOut)
async def registration(user: Annotated[shemas.UserReg, Body()], user_service: Annotated[UserService, Depends(user_service)]):
    return user_service.sign_up(user) 


@app.post("/create_smart_module", response_model=shemas.SmartModule)
async def create_smart_module(smart_module: Annotated[shemas.SmartModule, Body()], smart_module_service: Annotated[SmartModuleService, Depends(smart_module_service)]):
    return smart_module_service.create(smart_module) 

@app.post("/start_workout")
async def start_workout(workout: Annotated[shemas.Workout, Body()], workout_service: Annotated[WorkoutService, Depends(workout_service)]):
    workout_service.start(workout)
    return {"message": "workout starts!"}

@app.post("/end_workout")
async def end_workout(user_id: int, identification_key: str, workout_service: Annotated[WorkoutService, Depends(workout_service)]):
    workout_service.end(user_id, identification_key)
    return {"message": "workout ends!"}

@app.post("/public_pull_ups")
async def public_pull_ups(data: Annotated[shemas.PublicPullUps, Body()],   workout_service: Annotated[WorkoutService, Depends(workout_service)]):
    status = workout_service.update_pulls(data)
    if status:
        return {"message": "pull ups counted"}
    else:
        return {"message": "pull ups doesnt counted"
                           ""}
