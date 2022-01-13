from schemas import User
from fastapi import APIRouter, status, UploadFile, File, Form, Depends
import sys

sys.path.append("../")
from oauth2 import oauth2_scheme

router = APIRouter(prefix="/users", tags=["users"])


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_user(
    user: User = Form(...), file: UploadFile = File(...)
):
    return {
        "name": user.name,
        "email": user.email,
        "filename": file.filename,
    }


@router.get("")
async def get_all_users(token: str = Depends(oauth2_scheme)):
    return {"token": token}
