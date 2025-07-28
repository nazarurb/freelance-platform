from functools import wraps
from typing import Callable

from fastapi import HTTPException, status

from app.database.models import User
from app.utils.logger import admin_logger


def admin_required(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        current_user = kwargs.get("current_user")

        if not isinstance(current_user, User) or current_user.role != "admin":
            admin_logger.warning(
                f"❌ UNAUTHORIZED ACCESS | User ID: {getattr(current_user, 'id', 'Unknown')} | "
                f"Route: {func.__name__}"
            )
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You don't have permission to access this resource"
            )

        admin_logger.info(
            f"✅ ACCESS ALLOWED | Admin ID: {current_user.id} | Execution: {func.__name__}"
        )
        return func(*args, **kwargs)

    return wrapper
