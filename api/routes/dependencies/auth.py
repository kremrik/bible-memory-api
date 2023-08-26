from schemas.jwt import JWT
from authorization.jwt_auth import validate_token

from fastapi import Depends, HTTPException, status


__all__ = ["validate_admin_user", "validate_user"]


validate_user = validate_token


async def validate_admin_user(
    user: JWT = Depends(validate_token),
) -> JWT:
    unauthorized_exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="User must be an admin to access this route",
    )

    if not user.admin:
        raise unauthorized_exception

    return user
