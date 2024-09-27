from sqlalchemy.orm import Session
from models.studentModel import StudentModel
from schemas.studentSchema import StudentCreate

def create_student(db: Session, student: StudentCreate):
    db_student = StudentModel(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_all_students(db: Session):
    return db.query(StudentModel).all()

def search_students(db: Session, search: str):
    search = f"%{search}%"
    return db.query(StudentModel).filter(
        (StudentModel.cpf.like(search)) |
        (StudentModel.name.like(search)) |
        (StudentModel.cellphone.like(search))
    ).all()