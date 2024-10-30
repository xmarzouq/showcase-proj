from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from backend.app.db.db import SessionLocal
from backend.app.db.repo import add_student

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Student(BaseModel):
    name: str
    email: str
    teacher_ids: list[int] | None


@router.post("/student")
async def create_student(student: Student, db: Session = Depends(get_db)):
    result = add_student(db, student.dict(), teacher_ids=student.teacher_ids)
    if result:
        return {"message": "Student added successfully", "student": result}
    raise HTTPException(
        status_code=400, detail="Failed to add student; email might already be in use."
    )
