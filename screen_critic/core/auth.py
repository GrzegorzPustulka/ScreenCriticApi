from datetime import datetime, timedelta
from typing import MutableMapping

from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from sqlalchemy.orm.session import Session

from screen_critic.models import User

from .config import settings
from .security import verify_password

JWTPayloadMapping = MutableMapping[str, datetime | bool | str | list[str] | list[int]]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"/auth/login")


def authenticate(
    username: str,
    password: str,
    db: Session,
) -> User | None:
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user


def create_access_token(sub: str) -> str:
    return _create_token(
        token_type="access_token",
        lifetime=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        sub=sub,
    )


def _create_token(
    token_type: str,
    lifetime: timedelta,
    sub: str,
) -> str:
    payload = {}
    expire = datetime.utcnow() + lifetime
    payload["type"] = token_type
    payload["exp"] = expire
    payload["iat"] = datetime.utcnow()
    payload["sub"] = str(sub)

    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM)
