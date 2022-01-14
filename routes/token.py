from database import get_db
from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm.session import Session
from schemas import Token
from fastapi.security import OAuth2PasswordRequestForm
from oauth2 import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    create__access_token,
    authenticate_user,
)
from datetime import timedelta

router = APIRouter(tags=["token"])


@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    access_token = create__access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
