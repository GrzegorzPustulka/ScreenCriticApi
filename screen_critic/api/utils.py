from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from screen_critic.crud.user import user as crud_user
from screen_critic.schemas.user import UserCreate, UserUpdate


def check_user_existence(db: Session, user_in: UserCreate | UserUpdate):
    user = crud_user.get_by_email(db, user_in.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="The user with this email already exists in the system",
        )
    user = crud_user.get_by_username(db, user_in.username)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="The user with this username already exists in the system",
        )
