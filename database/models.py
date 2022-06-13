from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime, ForeignKey, Date
from database import engine

base = declarative_base()

class Employee(base):
    __tablename__ = 'employees'

    employee_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(16), nullable=False)
    last_name = Column(String(16), nullable=False)
    date = Column(Date(), nullable=False)


base.metadata.create_all(engine)