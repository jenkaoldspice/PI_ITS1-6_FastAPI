from typing import Optional
from pydantic import BaseModel, EmailStr, HttpUrl
from datetime import datetime


class Employee(BaseModel):
    id: Optional[int] = None
    name: str
    surname: str
    email: EmailStr
    updated_at: datetime
    created_at: datetime


class EmployeeIn(BaseModel):
    name: str
    surname: str
    email: EmailStr

class EmployeeImage(BaseModel):
    url: HttpUrl
    name: str
    type: str
    creation_date: datetime