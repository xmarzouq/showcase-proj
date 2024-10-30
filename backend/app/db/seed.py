from sqlalchemy import text
from sqlalchemy.orm import Session
from backend.app.db.db import SessionLocal, initialize_db
from backend.app.db.repo import add_teacher, add_student
from faker import Faker
from backend.app.core.enums import random_subject


def seed_data():
    db: Session = SessionLocal()
    fake = Faker()
    try:
        db.execute(text("DELETE FROM teacher_student"))
        db.execute(text("DELETE FROM students"))
        db.execute(text("DELETE FROM teachers"))
        db.commit()
        teachers = []
        for _ in range(5):
            teacher = add_teacher(
                db, {"name": fake.name(), "subject": random_subject()}
            )
            teachers.append(teacher)

        for _ in range(5):
            student = add_student(
                db,
                {"name": fake.name(), "email": fake.email()},
                teacher_ids=[
                    teacher.id
                    for teacher in fake.random_elements(
                        elements=teachers, length=fake.random_int(min=1, max=3)
                    )
                ],
            )

    finally:
        db.close()


initialize_db()
seed_data()