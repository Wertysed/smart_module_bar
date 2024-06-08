from pydantic import BaseModel



class SmartModule(BaseModel):
    identification: str
    session_status: int
    user_id: int

