from sqlalchemy import String
from sqlalchemy.orm import mapped_column, relationship

from screen_critic.models.base import Base


class Category(Base):
    name = mapped_column(String(50), nullable=True)

    # Relationships
    movies = relationship("Movie", back_populates="category")

    def __repr__(self):
        return f"<Category(Name='{self.name}')>"
