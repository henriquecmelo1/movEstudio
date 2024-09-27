from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from schemas.studentSchema import StudentCreate, Student
from services.student_service import create_student, get_all_students, search_students
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

# @router.get("/{student_id}")
# def get_student_by_id(student_id: int) -> Student:
#     db = get_db()
#     target_student = (
#         db.query(Student)
#         .filter(Student.id == student_id)
#     )

#     if not target_student.first():
#         raise HTTPException(status_code=404, detail="Student not found")
#     return target_student.first()
    
