from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from domains.employee import Employee, EmployeeIn
from repositories import employees
from .depends import get_employee_repository
from repositories.employees import EmployeeRepository
router = APIRouter()

@router.get("/all")
async def read_employees(
        employees: EmployeeRepository = Depends(get_employee_repository),
        limit: int = 100,
        skip: int = 100):
    return await employees.get_all(limit=limit, skip=0)


@router.post("/sign-up", response_model=Employee)
async def create(employee: EmployeeIn, employees: EmployeeRepository = Depends(get_employee_repository)):
    return await employees.create(u=employee)

@router.delete("/delete")
async def delete(id: int, employees: EmployeeRepository = Depends(get_employee_repository)) -> Employee:
    nf_exception = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
    result = await employees.delete(id=id)
    if result is None:
        raise nf_exception
    return {"status": True}