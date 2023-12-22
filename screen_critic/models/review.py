from sqlalchemy import Date, Float, ForeignKey, Integer, Text
from sqlalchemy.orm import mapped_column, relationship

from screen_critic.models.base import Base


class Review(Base):
    rating = mapped_column(Float, nullable=True)
    comment = mapped_column(Text, nullable=True)
    date = mapped_column(Date, nullable=True)
    user_id = mapped_column(Integer, ForeignKey("user.id"))
    movie_id = mapped_column(Integer, ForeignKey("movie.id"))

    user = relationship("User", back_populates="reviews")
    movie = relationship("Movie", back_populates="reviews")

    def __repr__(self):
        return f"<Review(Rating='{self.rating}', Comment='{self.comment}', Date='{self.date}', User_ID='{self.user_id}', Movie_ID='{self.movie_id}')>"
