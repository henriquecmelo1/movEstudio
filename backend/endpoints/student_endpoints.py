from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from schemas.studentSchema import StudentCreate, Student
from services.student_service import create_student, get_all_students, search_students, delete_student
from db.session import get_db

router = APIRouter()

@router.post("/", response_model=Student)
def create_new_student(student: StudentCreate, db: Session = Depends(get_db)):
    return create_student(db=db, student=student)


@router.get("/", response_model=list[Student])
def read_students(search: str = Query(None), db: Session = Depends(get_db)):
    if search:
        return search_students(db=db, search=search)
    return get_all_students(db=db)

@router.delete("/{cpf}")
def delete_student_by_cpf(cpf: str, db: Session = Depends(get_db)):
    return delete_student(db=db, student_cpf=cpf)


