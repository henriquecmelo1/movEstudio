from models.studentModel import StudentModel

def serializer_student(student: StudentModel) -> dict:
    return {
        "cpf": student["cpf"],
        "name": student["name"],
        "birthday": student["birthday"],
        "cellphone": student["cellphone"],
        "payment_day": student["payment_day"],
        "payment_value": student["payment_value"],
        "frequency": student["frequency"],
        "appointment_day": student["appointment_day"],
        "appointment_time": student["appointment_time"],
        "emergency_contact": student["emergency_contact"],
    }

def serializer_students_list(students: list[StudentModel]) -> list[dict]:
    return [serializer_student(student) for student in students]

