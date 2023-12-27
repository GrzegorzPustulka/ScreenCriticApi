from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from screen_critic.api.deps import get_db
from screen_critic.crud.user import user as crud_user
from screen_critic.schemas.user import UserRead

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/id/{user_id}", response_model=UserRead, status_code=status.HTTP_200_OK)
async def read_user(user_id: str, db: Session = Depends(get_db)):
    user = crud_user.get(db, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return UserRead(**jsonable_encoder(user))


@router.get("/name/{username}", response_model=UserRead, status_code=status.HTTP_200_OK)
async def read_user_by_name(username: str, db: Session = Depends(get_db)):
    user = crud_user.get_by_username(db, username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return UserRead(**jsonable_encoder(user))
