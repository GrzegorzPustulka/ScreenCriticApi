from sqlalchemy.orm import Session

from screen_critic.core.security import get_password_hash
from screen_critic.models import User
from screen_critic.schemas.user import UserCreate, UserUpdate

from .base import CRUDBase


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    @staticmethod
    def get_by_email(db: Session, email: str) -> User | None:
        return db.query(User).filter(User.email == email).one_or_none()

    @staticmethod
    def get_by_username(db: Session, username: str) -> User | None:
        return db.query(User).filter(User.username == username).one_or_none()

    def create(self, db: Session, obj_in: UserCreate) -> User:
        create_data = obj_in.model_dump()
        create_data.pop("hashed_password")
        db_obj = User(**create_data)
        db_obj.hashed_password = get_password_hash(obj_in.hashed_password)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


user = CRUDUser(User)
