from uuid import UUID

from pydantic import BaseModel


class CategoryRead(BaseModel):
    id: UUID
    name: str


class CategoryCreate(CategoryRead):
    raise NotImplementedError


class CategoryUpdate(CategoryRead):
    raise NotImplementedError
