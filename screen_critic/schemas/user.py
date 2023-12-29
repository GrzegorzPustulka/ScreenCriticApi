from typing import Literal
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


class UserRead(BaseModel):
    id: UUID
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    rank: Literal["user", "reviewer"]


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    hashed_password: str = Field(alias="password")
    first_name: str
    last_name: str
    rank: Literal["user", "reviewer"]


class UserUpdate(BaseModel):
    hashed_password: str | None
    first_name: str | None
    last_name: str | None
