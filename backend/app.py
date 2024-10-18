from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from endpoints.student_endpoints import router

app = FastAPI()

app.include_router(router, prefix="/students")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # URL do Angular
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


