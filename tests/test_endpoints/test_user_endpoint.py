import uuid

from fastapi import status
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from screen_critic.crud.user import user as crud_user
from screen_critic.models import User
from tests.conftest import client, db


def test_get_user_by_id(client: TestClient, db: Session):
    id = crud_user.get_by_email(db, "email_1@gmail.com").id
    response = client.get(f"/user/{id}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["id"] == str(id)
    assert response.json()["username"] == "username_1"


def test_invalid_get_user_by_id(client: TestClient, db: Session):
    id = uuid.uuid4()
    response = client.get(f"/user/{str(id)}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
