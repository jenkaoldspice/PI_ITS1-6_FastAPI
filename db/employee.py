from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey, URL
from datetime import datetime
from .base import metadata

employee = Table(
    "employee",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True, unique=True),
    Column("email", String, unique=True),
    Column("name", String),
    Column("surname", String),
    Column("position", String),
    Column("avatar_link", String),
    Column("created_at", DateTime, default=datetime.utcnow),
    Column("updated_at", DateTime, default=datetime.utcnow)
)
