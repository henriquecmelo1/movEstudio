
from pydantic import BaseModel


class Student(BaseModel):
    cpf: str
    name: str
    birthday: str
    cellphone: str
    payment_day: int
    payment_value: float
    frequency: int
    appointments: str
    emergency_contact: str
    