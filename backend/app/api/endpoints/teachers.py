from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.db.db import SessionLocal
from backend.app.db.repo import get_all_teachers

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/teachers")
def get_teachers(db: Session = Depends(get_db)):
    teachers = get_all_teachers(db)
    if not teachers:
        raise HTTPException(status_code=404, detail="No teachers!!!!")
    return teachers