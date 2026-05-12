from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.group_router import router as group_router
from app.api.student_router import router as student_router
from app.db.database import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(
    title="Students API",
    lifespan=lifespan,
)


app.include_router(student_router)
app.include_router(group_router)


@app.get("/")
def root():
    return {"message": "Students API is running"}
