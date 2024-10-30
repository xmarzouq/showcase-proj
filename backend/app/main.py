from fastapi import FastAPI
from backend.app.api.endpoints import teachers, students
from backend.app.db.seed import seed_data

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    seed_data()

app.include_router(teachers.router)
app.include_router(students.router)