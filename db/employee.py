from sqlalchemy import Table, Column, Integer, String, Boolean, DateTime
from datetime import datetime

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