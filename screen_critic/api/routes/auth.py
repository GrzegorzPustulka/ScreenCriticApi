from fastapi import APIRouter, Depends, HTTPException, status

from screen_critic.api.deps import get_db
from screen_critic.schemas.user import UserRead, UserCreate

router = APIRouter()


@router.get("/me", response_model=UserRead, status_code=status.HTTP_200_OK)
async def read_user_me(db=Depends(get_db), user_in=UserCreate):
    return {"user_id": "me"}
