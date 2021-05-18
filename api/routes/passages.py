from api.routes.dependencies import validate_user
from api.utils.request import request
from app.passage import get_passage
from schemas.response.passages import BibleResponse

from fastapi import APIRouter, Depends


__all__ = ["router"]


router = APIRouter()
tags = ["passages"]


@router.get(
    "/passages/{passage}", response_model=BibleResponse, tags=tags
)
async def passages(
    passage: str,
    user=Depends(validate_user),
):
    response = await request(passage)
    data = get_passage(response)
    return data
