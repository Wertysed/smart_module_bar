from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db import Base

class Sex(Base):
    __tablename__ = "sex"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    athlete = relationship("Athlete", back_populates="sex")


