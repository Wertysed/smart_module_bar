from sqlalchemy import Column, ForeignKey, Integer, String

from db import Base


class SmartModule(Base):
    __tablename__ = 'smart_module'

    id = Column(Integer, primary_key=True, index=True)
    identification = Column(String, index=True)
    session_status = Column(Integer, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

