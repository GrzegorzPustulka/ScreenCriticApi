from sqlalchemy import Enum, String
from sqlalchemy.orm import mapped_column, relationship

from .base import Base


class User(Base):
    username = mapped_column(String(50), unique=True, nullable=False)
    email = mapped_column(String(50), unique=True, nullable=False)
    hashed_password = mapped_column(String, nullable=False)
    first_name = mapped_column(String(50), nullable=False)
    last_name = mapped_column(String(50), nullable=False)
    rank = mapped_column(
        Enum("user", "reviewer", name="user_rank_enum"), nullable=False
    )

    # Relationships
    reviews = relationship("Review", back_populates="user")
    movie_lists = relationship("MovieList", back_populates="user")
    rates = relationship("Rate", back_populates="user")

    def __repr__(self) -> str:
        return (
            f"<User(id={self.id!r}, username={self.username!r}, email={self.email!r}, "
            f"hashed_password={self.hashed_password!r}, first_name={self.first_name!r}, "
            f"last_name={self.last_name!r})>"
        )
