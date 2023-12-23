from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from screen_critic.api.deps import get_db
from screen_critic.crud.user import user as crud_user
from screen_critic.schemas.user import UserCreate, UserRead, UserUpdate

from ..utils import check_user_existence

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/{user_id}", response_model=UserRead, status_code=status.HTTP_200_OK)
async def read_user(user_id: str, db: Session = Depends(get_db)):
    user = crud_user.get(db, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return UserRead(**jsonable_encoder(user))


@router.patch("/{user_id}", response_model=UserRead, status_code=status.HTTP_200_OK)
def update_user(user_id: str, user_in: UserUpdate, db: Session = Depends(get_db)):
    check_user_existence(db, user_in)
    user = crud_user.update(db, user_id, user_in)
    return UserRead(**jsonable_encoder(user))

