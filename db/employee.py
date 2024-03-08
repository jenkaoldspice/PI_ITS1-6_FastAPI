from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from datetime import datetime

from sqlalchemy_media import Image

from domains.employee import Employee
from .base import metadata

employee = Table(
    "employee",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True, unique=True),
    Column("email", String, unique=True),
    Column("name", String),
    Column("surname", String),
    Column("created_at", DateTime, default=datetime.utcnow),
    Column("updated_at", DateTime, default=datetime.utcnow)
)

images = Image(
    "image",
    metadata,
    Column("employee", Integer, ForeignKey(Employee.id), primary_key=True,),
    Column("name", String(50), primary_key=True),
    Column("filetype", String(50))
)
