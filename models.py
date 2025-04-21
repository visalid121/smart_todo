from sqlalchemy import Column, Integer, String, DateTime, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    deadline = Column(DateTime)
    priority = Column(Integer, default=1)
    category = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    completed = Column(Boolean, default=False)
