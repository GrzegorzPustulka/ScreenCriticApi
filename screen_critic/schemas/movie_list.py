from uuid import UUID

from pydantic import BaseModel


class MovieListCreate(BaseModel):
    id: UUID
