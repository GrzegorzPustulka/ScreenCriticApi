from sqlalchemy import Date, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import mapped_column, relationship

from screen_critic.models.base import Base


class Movie(Base):
    title = mapped_column(String(50))
    director = mapped_column(String(50), nullable=True)
    release_date = mapped_column(Date, nullable=True)
    description = mapped_column(Text, nullable=True)
    average_rating = mapped_column(Float, nullable=True)
    category_id = mapped_column(Integer, ForeignKey("category.id"), nullable=True)

    # Relationships
    reviews = relationship("Review", back_populates="movie")
    movie_lists = relationship("MovieList", back_populates="movie")
    rates = relationship("Rate", back_populates="movie")
    category = relationship("Category", back_populates="movies")

    def __repr__(self):
        return f"<Movie(Title='{self.title}', Director='{self.director}', Release_Date='{self.release_date}', Description='{self.description}', Average_Rating='{self.average_rating}', Category_ID='{self.category_id}')>"
