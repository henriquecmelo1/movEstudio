from app import app
from models.studentModel import StudentModel

@app.get("/")
async def root():
    return {"Hello": "World"}

# students = []

# @app.get("/students")
# async def get_all_students():
#     return {"students": students}

# @app.post("/students")
# async def create_student(student: StudentModel):
#     students.append(student)
#     return {"message": "Student created successfully"}

# @app.get("/students/{cpf}")
# async def get_student(cpf: str):
#     for student in students:
#         if student.cpf == cpf:
#             return {"student": student}

# @app.put("/students/{cpf}")
# async def update_student(cpf: str, student: StudentModel):
#     for i in students:
#         if i.cpf == cpf:
#             i.name = student.name
#             i.birthday = student.birthday
#             i.cellphone = student.cellphone
#             i.payment_day = student.payment_day
#             i.payment_value = student.payment_value
#             i.frequency = student.frequency
#             i.appointments = student.appointments
#             i.emergency_contact = student.emergency_contact
            
#             return {"message": "Student updated successfully"}
#     return {"message": "Student not found"}

# @app.delete("/students/{cpf}")
# async def delete_student(cpf: str):
#     for student in students:
#         if student.cpf == cpf:
#             students.remove(student)
#             return {"message": "Student deleted successfully"}
#     return {"message": "Student not found"}
    