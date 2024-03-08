from fastapi import Depends, HTTPException, status
from domains.employee import Employee
from repositories.employees import EmployeeRepository
from db.base import database


def get_user_repository() -> EmployeeRepository:
    return EmployeeRepository(database)