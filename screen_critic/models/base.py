import uuid

from sqlalchemy import UUID
from sqlalchemy.orm import DeclarativeBase, declared_attr, mapped_column


class Base(DeclarativeBase):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = mapped_column(
        UUID, primary_key=True, nullable=False, unique=True, default=uuid.uuid4
    )
