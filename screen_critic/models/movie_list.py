from sqlalchemy import UUID, Date, ForeignKey
from sqlalchemy.orm import mapped_column, relationship

from screen_critic.models.base import Base


class MovieList(Base):
    date_added = mapped_column(Date, nullable=False)
    movie_id = mapped_column(UUID, ForeignKey("movie.id"))
    user_id = mapped_column(UUID, ForeignKey("user.id"))

    # Relationships
    user = relationship("User", back_populates="movie_lists")
    movie = relationship("Movie", back_populates="movie_lists")

    def __repr__(self):
        return f"<MovieList(Date_Added='{self.date_added}', Movie_ID='{self.movie_id}', User_ID='{self.user_id}')>"
