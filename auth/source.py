import uuid
from fastapi import Request
from fastapi_users import FastAPIUsers
from auth.manager import get_user_manager
from models.user_model import User
from auth.auth import auth_backend


fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)


async def get_enabled_backends(request: Request):
    """Return the enabled dependencies following custom logic."""
    if request.url.path == "/protected-route-only-jwt":
        return [auth_backend]
    else:
        return [auth_backend]


current_active_user = fastapi_users.current_user(active=True, get_enabled_backends=get_enabled_backends)
