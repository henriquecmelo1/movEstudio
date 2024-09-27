from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.studentSchema import StudentCreate, Student
from services.student_service import create_student, get_all_students
from db.session import get_db

router = APIRouter()

@router.post("/", response_model=Student)
def create_new_student(student: StudentCreate, db: Session = Depends(get_db)):
    return create_student(db=db, student=student)

@router.get("/", response_model=list[Student])
def read_students(db: Session = Depends(get_db)):
    return get_all_students(db=db)
