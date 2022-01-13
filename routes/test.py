from fastapi import APIRouter
from typing import Optional

router = APIRouter(prefix="/test", tags=["tests"])


@router.get("/{item_id}")
async def read_user_item(
    item_id: int, needy: str, skip: int = 0, limit: Optional[int] = None
):
    return {
        "item_id": item_id,
        "needy": needy,
        "skip": skip,
        "limit": limit,
    }
