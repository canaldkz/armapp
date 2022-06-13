# from sqlalchemy.exc import IntegrityError
from database import with_session
from database.models import *

@with_session
def add_employee(first_name, last_name, datetime, session):
    emp = Employee(first_name=first_name, last_name=last_name, datetime=datetime)
    session.add(emp)
    return (True, 'Ok!')


@with_session
def get_all_employees(session):
    result = session.query(Employee).all()
    return (True, result) if result else (False, 'Нет работников')
