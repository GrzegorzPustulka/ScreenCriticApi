from abc import ABC, abstractmethod
from typing import Literal
from uuid import UUID

from screen_critic.models import Category, Movie, User, MovieList, Rate, Review


class Factory(ABC):
    @staticmethod
    @abstractmethod
    def create(**kwargs) -> object:
        pass


class MovieFactory(Factory):
    @staticmethod
    def create(
        title: str,
        director: str,
        release_date: str,
        description: str,
        average_rating: float,
        category_id: UUID,
    ) -> Movie:
        return Movie(
            title=title,
            director=director,
            release_date=release_date,
            description=description,
            average_rating=average_rating,
            category_id=category_id,
        )


class CategoryFactory(Factory):
    @staticmethod
    def create(name: str) -> Category:
        return Category(name=name)


class UserFactory(Factory):
    @staticmethod
    def create(
        username: str,
        email: str,
        hashed_password: str,
        first_name: str,
        last_name: str,
        rank: Literal["user", "reviewer"],
    ) -> User:
        return User(
            username=username,
            email=email,
            hashed_password=hashed_password,
            first_name=first_name,
            last_name=last_name,
            rank=rank,
        )


class MovieListFactory(Factory):
    @staticmethod
    def create(date_added: str, movie_id: UUID, user_id: UUID) -> MovieList:
        return MovieList(date_added=date_added, movie_id=movie_id, user_id=user_id)


class RateFactory(Factory):
    @staticmethod
    def create(rating: float, user_id: UUID, movie_id: UUID) -> Rate:
        return Rate(rating=rating, user_id=user_id, movie_id=movie_id)


class ReviewFactory(Factory):
    @staticmethod
    def create(
        rating: float, comment: str, date: str, user_id: UUID, movie_id: UUID
    ) -> Review:
        return Review(
            rating=rating,
            comment=comment,
            date=date,
            user_id=user_id,
            movie_id=movie_id,
        )
