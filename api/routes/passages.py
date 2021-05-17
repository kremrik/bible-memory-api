from api.routes.dependencies import validate_user
from api.utils.request import request
from app.passage import get_passage
from schemas.passages import BibleResponse

from fastapi import APIRouter, Depends


__all__ = ["router"]


router = APIRouter()


@router.get("/passage/{passage}", response_model=BibleResponse)
async def passage(
    passage: str,
    username=Depends(validate_user),
):
    response = await request(passage)
    data = get_passage(response)
    return data
