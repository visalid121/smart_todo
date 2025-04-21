from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
from models import Task
from datetime import datetime
from test_suggestion import get_suggestions

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/tasks/")
def create_task(title: str, deadline: str, category: str, db: Session = Depends(get_db)):
    deadline_dt = datetime.fromisoformat(deadline)
    task = Task(title=title, deadline=deadline_dt, category=category)
    db.add(task)
    db.commit()
    return {"message": "Task added"}

@app.get("/tasks/")
def read_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()

@app.get("/suggestions/")
def get_task_suggestions(count: int = 3):
    """Get task suggestions for the user."""
    return get_suggestions(count)

@app.get("/")
def root():
    return {"message": "Smart Todo API is running!"}
