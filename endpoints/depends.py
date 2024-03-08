from repositories.employees import EmployeeRepository
from db.base import database


def get_employee_repository() -> EmployeeRepository:
    return EmployeeRepository(database)
