from typing import Optional

from pydantic import BaseModel, EmailStr


class UserType(BaseModel):
    username: str
    email: EmailStr

    class Config:
        orm_mode = True


class UserInDB(UserType):
    hashed_password: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    name: Optional[str] = None
