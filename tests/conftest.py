import random

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from screen_critic.api.deps import get_db
from screen_critic.core.config import settings
from screen_critic.core.security import get_password_hash
from screen_critic.main import app
from screen_critic.models import Base, User

from .command import CreateObjectCommand
from .factory import (CategoryFactory, MovieFactory, MovieListFactory,
                      RateFactory, ReviewFactory, UserFactory)

SQLALCHEMY_DATABASE_URI = f"postgresql://postgres:{settings.db_password.get_secret_value()}@localhost:5432/tests"
engine = create_engine(SQLALCHEMY_DATABASE_URI)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="module")
def db() -> Session:
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    setup_db(db)
    db.commit()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="module")
def client(db: Session) -> TestClient:
    def override_get_db():
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c


def setup_db(db: Session):
    categories = [
        CreateObjectCommand(db, CategoryFactory, name=f"Name_{i}").execute()
        for i in range(5)
    ]
    categories_id = [category.id for category in categories]

    movies = [
        CreateObjectCommand(
            db,
            MovieFactory,
            title=f"Movie_{i}",
            director=f"Director_{i}",
            release_date=f"2021-01-01",
            description=f"Description_{i}",
            average_rating=random.uniform(1, 10),
            category_id=random.choice(categories_id),
        ).execute()
        for i in range(20)
    ]
    movies_id = [movie.id for movie in movies]
    users = [
        CreateObjectCommand(
            db,
            UserFactory,
            username=f"Username_{i}",
            email=f"E-mail_{i}@gmail.com",
            hashed_password=f"{get_password_hash('hashed_password')}",
            first_name=f"First_Name_{i}",
            last_name=f"Last_Name_{i}",
            rank="user" if random.random() < 0.5 else "reviewer",
        ).execute()
        for i in range(10)
    ]
    users_id = [user.id for user in users]

    _ = [
        CreateObjectCommand(
            db,
            MovieListFactory,
            date_added=f"2021-01-01",
            movie_id=movies_id[i],
            user_id=users_id[0],
        ).execute()
        for i in range(5)
    ]

    _ = [
        CreateObjectCommand(
            db,
            RateFactory,
            rating=random.uniform(1, 10),
            user_id=users_id[i],
            movie_id=movies_id[0],
        ).execute()
        for i in range(5)
    ]

    _ = [
        CreateObjectCommand(
            db,
            ReviewFactory,
            rating=random.uniform(1, 10),
            comment=f"Comment_{i}",
            date=f"2021-01-01",
            user_id=users_id[1],
            movie_id=movies_id[0],
        ).execute()
        for i in range(5)
    ]
