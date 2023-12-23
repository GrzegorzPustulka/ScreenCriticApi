import random

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from screen_critic.api.deps import get_db
from screen_critic.core.config import settings
from screen_critic.main import app
from screen_critic.models import Base, User

SQLALCHEMY_DATABASE_URI = f"postgresql://postgres:{settings.db_password.get_secret_value()}@localhost:5432/tests"
engine = create_engine(SQLALCHEMY_DATABASE_URI)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="module")
def db() -> Session:
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    for i in range(10):
        rank = "user" if random.random() > 0.5 else "reviewer"
        db.add(
            User(
                username=f"username_{i}",
                email=f"email_{i}@gmail.com",
                hashed_password=f"hashed_password_{i}",
                first_name=f"grzegorz_{i}",
                last_name=f"Pustulka_{i}",
                rank=rank,
            )
        )
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
