from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime


class Employee(BaseModel):
    id: Optional[int] = None
    name: str
    surname: str
    email: EmailStr
    updated_at: datetime
    created_at: datetime
