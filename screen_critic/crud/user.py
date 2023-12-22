from sqlalchemy.orm import Session

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


user = CRUDUser(User)
