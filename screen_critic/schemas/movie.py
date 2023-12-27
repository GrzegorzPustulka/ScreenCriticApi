from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class CategoryRead(BaseModel):
    category_name: str | None = None


class MovieCreate(CategoryRead):
    pass


class MovieUpdate(CategoryRead):
    pass


class MovieRead(CategoryRead):
    id: UUID
    title: str
    director: str | None = None
    release_date: datetime | None | str = None
    description: str | None = None
    average_rating: float | None = None
