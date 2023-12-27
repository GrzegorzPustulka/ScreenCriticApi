from sqlalchemy import func
from sqlalchemy.orm import Session

from screen_critic.crud.base import CRUDBase
from screen_critic.models import Movie
from screen_critic.schemas.movie import MovieCreate, MovieUpdate


class CRUDMovie(CRUDBase[Movie, MovieCreate, MovieUpdate]):
    @staticmethod
    def get_by_name(db: Session, title: str) -> list[Movie]:
        return db.query(Movie).filter(Movie.title == title).all()

    @staticmethod
    def get_random(db: Session, category_id: str = None):
        return (
            db.query(Movie)
            .filter(Movie.average_rating >= 7.5, Movie.category_id == category_id)
            .order_by(func.random())
            .first()
        )


movie = CRUDMovie(Movie)
