from sqlalchemy import  Integer, String, Float, Date, Time
from db.base import Base
from sqlalchemy.sql import func
from sqlalchemy.types import Enum
from sqlalchemy.orm import mapped_column, Mapped
import enum

class WeekDays(str, enum.Enum):
        MONDAY = "Segunda-Feira"
        TUESDAY = "Terça-Feira"
        WEDNESDAY = "Quarta-Feira"
        THURSDAY = "Quinta-Feira"
        FRIDAY = "Sexta-Feira"
        SATURDAY = "Sábado"
        SUNDAY = "Domingo"

class StudentModel(Base):
    __tablename__ = 'students'
    
    cpf: Mapped[str] = mapped_column(String(11), primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    birthday: Mapped[Date] = mapped_column(Date, nullable=False, default=func.current_date())
    cellphone: Mapped[str] = mapped_column(String(11), nullable=False)
    payment_day: Mapped[int] = mapped_column(Integer, default=1)
    payment_value: Mapped[float] = mapped_column(Float, default=0.0)
    frequency: Mapped[int] = mapped_column(Integer, default=1)
    appointment_day: Mapped[WeekDays] = mapped_column(Enum(WeekDays), nullable=False)
    appointment_time: Mapped[str] = mapped_column(Time, nullable=False)
    emergency_contact: Mapped[str] = mapped_column(String)
