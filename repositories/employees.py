from typing import List, Optional
from datetime import datetime

import sqlalchemy as sa

from db.employee import employee
from domains.employee import Employee, EmployeeIn
from .base import BaseRepository


class EmployeeRepository(BaseRepository):

    async def get_all(self, limit: int = 100, skip: int = 0) -> List[Employee]:
        query = employee.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def get_by_id(self, id: int) -> Optional[Employee]:
        query = employee.select().where(employee.c.id == id)
        employee_response = await self.database.fetch_one(query)
        if employee_response is None:
            return {
                "name": None,
                "surname": None,
                "email": None,
                "created_at": None,
                "updated_at": None}
        return Employee.parse_obj(employee_response)

    async def create(self, u: EmployeeIn) -> Employee:
        employee_dict = Employee(
            name=u.name,
            surname=u.surname,
            email=u.email,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )
        values = {**employee_dict.dict()}
        values.pop("id", None)
        query = employee.insert().values(**values)
        employee_dict.id = await self.database.execute(query)
        return employee_dict

    async def delete(self, id: int):
        query = employee.delete().where(employee.c.id == id)
        return await self.database.execute(query=query)
