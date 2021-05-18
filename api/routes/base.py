from api import __version__

from fastapi import APIRouter


__all__ = ["router"]


router = APIRouter()


@router.get("/", include_in_schema=False)
async def root():
    return {"message": __file__, "version": __version__}


@router.get("/status", include_in_schema=False)
async def status():
    return "ACTIVE"
