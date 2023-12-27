import uuid

from fastapi import status
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from screen_critic.crud.user import user as crud_user
from tests.conftest import client, db


def test_get_user_by_id(client: TestClient, db: Session):
    id = crud_user.get_by_email(db, "E-mail_1@gmail.com").id
    response = client.get(f"/user/id/{str(id)}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["id"] == str(id)
    assert response.json()["username"] == "Username_1"


def test_invalid_get_user_by_id(client: TestClient, db: Session):
    id = uuid.uuid4()
    response = client.get(f"/user/id/{str(id)}")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_get_user_by_username(client: TestClient, db: Session):
    response = client.get("/user/name/Username_1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["first_name"] == "First_Name_1"


def test_invalid_get_user_by_username(client: TestClient, db: Session):
    response = client.get("/user/name/dfef")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json()["detail"] == "User not found"
