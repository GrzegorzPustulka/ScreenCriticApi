from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, declared_attr, mapped_column


class Base(DeclarativeBase):
    """Base class for all models."""

    @declared_attr
    def __tablename__(cls):
        """Return the lowercase name of the class as the table name."""
        return cls.__name__.lower()

    id = mapped_column(Integer, primary_key=True, nullable=False, unique=True)
