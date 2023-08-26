from typing import Optional


__all__ = ["paginate_params"]


async def paginate_params(
    limit: Optional[int] = None, offset: Optional[int] = None
) -> dict:
    params = {"limit": limit or 10, "offset": offset or 0}

    return params
