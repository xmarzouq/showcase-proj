from functools import lru_cache
from sqlalchemy.orm import Session
from backend.app.db.models import Teacher, Student

@lru_cache()
def get_all_teachers(db: Session):
    return db.query(Teacher).all()


def add_teacher(db: Session, teacher_data):
    new_teacher = Teacher(**teacher_data)
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    return new_teacher

def add_student(db: Session, student_data: dict[str, str, list[int]], teacher_ids: list[int]):
    new_student = Student(name=student_data["name"], email=student_data["email"])
    
    if teacher_ids:
        new_student.teachers = db.query(Teacher).filter(Teacher.id.in_(teacher_ids)).all()
    
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student