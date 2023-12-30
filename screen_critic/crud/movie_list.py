from typing import Type

from sqlalchemy.orm import Session

from screen_critic.crud.base import CRUDBase
from screen_critic.models import MovieList
from screen_critic.schemas.movie_list import MovieListCreateInDb, MovieListUpdate


class CRUDMovieList(CRUDBase[MovieList, MovieListCreateInDb, MovieListUpdate]):
    @staticmethod
    def get_movie_list_by_user_id_and_movie_id(
        db: Session, user_id: str, movie_id: str
    ) -> MovieList | None:
        return (
            db.query(MovieList)
            .filter(MovieList.user_id == user_id, MovieList.movie_id == movie_id)
            .one_or_none()
        )

    @staticmethod
    def get_movie_list_by_user_id(db: Session, user_id: str) -> list[Type[MovieList]]:
        return db.query(MovieList).filter(MovieList.user_id == user_id).all()


movie_list = CRUDMovieList(MovieList)
