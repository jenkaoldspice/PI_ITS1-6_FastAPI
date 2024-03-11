from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime


class EmployeeIn(BaseModel):
    name: str
    surname: str
    position: str
    email: EmailStr
    avatar_link: Optional[str] = None


class Employee(BaseModel):
    id: Optional[int] = None
    name: str
    surname: str
    position: str
    email: EmailStr
    avatar_link: Optional[str] = None
    updated_at: datetime
    created_at: datetime
