from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from screen_critic.api.deps import get_current_user, get_db
from screen_critic.api.utils import check_user_existence
from screen_critic.core.auth import authenticate, create_access_token
from screen_critic.crud.user import user as crud_user
from screen_critic.models import User
from screen_critic.schemas.user import UserCreate, UserRead

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", status_code=status.HTTP_200_OK)
def login(
    db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    user = authenticate(username=form_data.username, password=form_data.password, db=db)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {
        "access_token": create_access_token(sub=user.id),
        "token_type": "bearer",
    }


@router.post("/signup", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user_signup(
    user_in: UserCreate,
    db: Session = Depends(get_db),
) -> Any:
    check_user_existence(db, user_in)
    user = crud_user.create(db=db, obj_in=user_in)

    return user


@router.get("/me", response_model=UserRead, status_code=status.HTTP_200_OK)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.delete("/me/delete", status_code=status.HTTP_204_NO_CONTENT)
def delete_account(current_user: User = Depends(get_current_user)):
    crud_user.remove(current_user.id)
