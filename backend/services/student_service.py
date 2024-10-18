from db.database import collection
from schemas.studentSchema import serializer_students_list

#------------GET---------------
def get_all_students():
    return serializer_students_list(collection.find())

def search_students(search: str):
    return serializer_students_list(collection.find({
        "$or": [
            {"cpf": {"$regex": search, "$options": "i"}},
            {"name": {"$regex": search, "$options": "i"}},
            {"cellphone": {"$regex": search, "$options": "i"}}
        ]
    }))

#------------POST---------------
def create_student(student: dict):
    collection.insert_one(student)

#------------PUT---------------
def update_student(cpf: str, student: dict):
    collection.update_one({"cpf": cpf}, {"$set": student})

#------------DELETE---------------
def delete_student(cpf: str):
    collection.delete_one({"cpf": cpf})

