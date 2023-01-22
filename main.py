import uuid
from fastapi import FastAPI
import uvicorn
from fastapi.routing import APIRouter
# from user.routes.user_routes import UserRoutes
from review.routes.review_routes import ReviewRoutes
from review.controllers.review_controller import ReviewController
# from user.controllers.user_controller import UserController
from auth.schemas import UserRead, UserCreate,UserUpdate
from auth.source import fastapi_users, auth_backend


app = FastAPI(title="HeavyReview")


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/auth",
    tags=["users"],
)

app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)

# uc = UserController()
# user_routes = UserRoutes(uc)

rc = ReviewController()
review_routes = ReviewRoutes(rc)

main_api_router = APIRouter()
# main_api_router.include_router(user_routes.router, prefix="/user", tags=["user"])
main_api_router.include_router(review_routes.router, prefix="/review", tags=["review"])
app.include_router(main_api_router, prefix="/api")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
