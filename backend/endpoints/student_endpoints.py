from fastapi import APIRouter
from models.studentModel import StudentModel
from services.student_service import search_students, get_all_students, create_student, update_student, delete_student


router = APIRouter()

@router.get("/", response_model=list[StudentModel])
async def get_students_endpoint(search: str = None):
    if search:
        return search_students(search)
    return get_all_students()

@router.post("/")
async def create_student_endpoint(student: StudentModel):
    return create_student(dict(student))

@router.put("/{cpf}")
async def update_student_endpoint(cpf: str, student: StudentModel):
    return update_student(cpf, dict(student))

@router.delete("/{cpf}")
async def delete_student_endpoint(cpf: str):
    return delete_student(cpf)






