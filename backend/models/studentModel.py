from datetime import date, time
from pydantic import BaseModel
import enum

# class WeekDays(str, enum.Enum):
#         MONDAY = "Segunda-Feira"
#         TUESDAY = "Terça-Feira"
#         WEDNESDAY = "Quarta-Feira"
#         THURSDAY = "Quinta-Feira"
#         FRIDAY = "Sexta-Feira"
#         SATURDAY = "Sábado"
#         SUNDAY = "Domingo"

class StudentModel(BaseModel):
    cpf: str
    name: str
    birthday: str
    cellphone: str
    payment_day: int
    payment_value: float
    frequency: int
    appointment_day: list
    appointment_time: list
    emergency_contact: str
