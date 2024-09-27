from sqlalchemy import Column, Integer, String, Float, Date
from db.base import Base
from sqlalchemy.sql import func


class StudentModel(Base):
    __tablename__ = "students"

    cpf = Column(String(11), primary_key=True, index=True)
    name = Column(String, nullable=False)
    birthday = Column(Date, nullable=False, default=func.current_date())
    cellphone = Column(String(11), nullable=False)
    payment_day = Column(Integer)
    payment_value = Column(Float)
    frequency = Column(Integer)
    appointments = Column(String)
    emergency_contact = Column(String)
