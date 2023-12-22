from pydantic import BaseModel


class UserRead(BaseModel):
    username: str
    email: str
    hashed_password: str
    first_name: str
    last_name: str


class UserCreate(BaseModel):
    username: str
    email: str
    hashed_password: str
    first_name: str
    last_name: str


class UserUpdate(BaseModel):
    hashed_password: str | None
    first_name: str | None
    last_name: str | None
