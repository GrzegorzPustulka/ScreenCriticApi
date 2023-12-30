from uuid import UUID

from pydantic import BaseModel

from .movie import MovieRead


class MovieListCreate(BaseModel):
    movie_id: UUID


class MovieListUpdate(BaseModel):
    pass


class MovieListRead(MovieRead):
    date_added: str


class MovieListCreateInDb(BaseModel):
    movie_id: UUID
    user_id: UUID
