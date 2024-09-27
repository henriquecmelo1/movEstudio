from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class StudentBase(BaseModel):
    cpf: str = Field(..., min_length=11, max_length=11, description="CPF deve ter 11 dígitos")
    name: str = Field(..., description="Nome do estudante")
    birthday: Optional[date] = Field(None, description="Data de nascimento")
    cellphone: str = Field(..., min_length=11, max_length=11, description="Número de telefone com 11 dígitos")
    payment_day: Optional[int] = Field(None, description="Dia do pagamento")
    payment_value: Optional[float] = Field(None, description="Valor do pagamento")
    frequency: Optional[int] = Field(None, description="Frequência de participação")
    appointments: Optional[str] = Field(None, description="Compromissos")
    emergency_contact: Optional[str] = Field(None, description="Contato de emergência")

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    class Config:
        orm_mode = True
