from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from db.connection import Base

class History(Base):
    __tablename__ = 'history'

    id = Column(Integer, primary_key=True, index=True)
    request_time = Column(DateTime, default=func.now())
    request = Column(String)
    response = Column(String)
