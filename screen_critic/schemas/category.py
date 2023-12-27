from uuid import UUID

from pydantic import BaseModel


class CategoryRead(BaseModel):
    id: UUID
    name: str


class CategoryCreate(CategoryRead):
    pass


class CategoryUpdate(CategoryRead):
    pass
