import sys
from typing import List

from database import get_db
from fastapi import APIRouter, Depends, status
from models import User
from schemas import UserInDB
from sqlalchemy.orm import Session

sys.path.append("../")
from oauth2 import get_password_hash, oauth2_scheme

router = APIRouter(prefix="/users", tags=["users"])


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_user(request: UserInDB, db: Session = Depends(get_db)):
    new_user = User(
        username=request.username,
        email=request.email,
        hashed_password=get_password_hash(request.hashed_password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("", response_model=List[UserInDB])
async def get_all_users(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
):
    return db.query(User).all()
