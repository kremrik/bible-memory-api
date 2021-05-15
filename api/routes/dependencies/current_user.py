from authentication.auth import get_current_active_user


__all__ = ["active_user"]


active_user = get_current_active_user
