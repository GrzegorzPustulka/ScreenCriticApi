from sqlalchemy import Float, ForeignKey, Integer
from sqlalchemy.orm import mapped_column, relationship

from screen_critic.models.base import Base


class Rate(Base):
    rating = mapped_column(Float, nullable=False)
    user_id = mapped_column(Integer, ForeignKey("user.id"))
    movie_id = mapped_column(Integer, ForeignKey("movie.id"))

    # Relationships
    user = relationship("User", back_populates="rates")
    movie = relationship("Movie", back_populates="rates")

    def __repr__(self):
        return f"<Rate(Rating='{self.rating}', User_ID='{self.user_id}', Movie_ID='{self.movie_id}')>"
