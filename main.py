from fastapi import FastAPI, Body, Depends
from typing import Annotated, Any
from sqlalchemy.orm import Session
import shemas, models, crud
from db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/login", response_model=shemas.UserOut)
async def login(user: Annotated[shemas.UserIn, Body()] = None):
    user_out = shemas.UserOut(**user.dict(), first_name="kaban")
    return user_out


@app.post("/registration", response_model=shemas.UserOut)
async def registration(user: Annotated[shemas.UserReg, Body()] = None, db: Session = Depends(get_db)):
    # hh = shemas.UserInDb(**user.dict(), hashed_password=user.password+'Hello')
    # print(hh)
    db_user = models.User(**(shemas.UserInDb(**user.dict(), hashed_password=user.password+'Hello')).dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return user

