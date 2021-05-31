from schemas.jwt import JWT
from api.routes.dependencies import validate_user
from api.utils.request import request
from app.passage import get_passage
from schemas.response.passages import (
    BibleResponse,
    AddPassageResponse,
)
from api.db.models.passages import Passages

from fastapi import APIRouter, Depends, HTTPException, status
from asyncpg.exceptions import UniqueViolationError  # type: ignore

import logging
from typing import List
from uuid import UUID


__all__ = ["router"]


LOGGER = logging.getLogger(__name__)


tags = ["passages"]
router = APIRouter(prefix="/passages", tags=tags)


@router.get("/", response_model=List[str])
async def get_passages(user: JWT = Depends(validate_user)):
    user_id = UUID(user.user_id)
    passages = (
        await Passages.select()
        .where(Passages.user_id == user_id)
        .run()
    )
    return [row["passage"] for row in passages]


@router.get(
    "/{passage}",
    response_model=BibleResponse,
    dependencies=[Depends(validate_user)],
)
async def fetch_passage(passage: str):
    response = await request(passage)
    data = get_passage(response)
    return data


@router.post("/{passage}", response_model=AddPassageResponse)
async def add_passage(
    passage: str, user: JWT = Depends(validate_user)
):
    user_id = user.user_id
    record = {"user_id": user_id, "passage": passage}
    try:
        await Passages.insert(Passages(**record)).run()  # type: ignore
        return record
    except UniqueViolationError as e:
        LOGGER.error(e)
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail=str(e)
        )
