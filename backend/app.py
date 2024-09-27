from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.base import Base
from db.session import engine
from endpoints import student_endpoints


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # URL do Angular
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(student_endpoints.router, prefix="/students")
