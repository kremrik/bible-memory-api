from api.routes.dependencies import validate_user
from api.utils.request import request
from app.passage import get_passage
from schemas.response.passages import BibleResponse

from fastapi import APIRouter, Depends


__all__ = ["router"]


tags = ["passages"]
router = APIRouter(prefix="/passages", tags=tags)


@router.get(
    "/{passage}",
    response_model=BibleResponse,
    dependencies=[Depends(validate_user)],
)
async def passages(passage: str):
    response = await request(passage)
    data = get_passage(response)
    return data
