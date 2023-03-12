import uuid
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi.openapi.models import Response
from fastapi.routing import APIRouter
# from user.routes.user_routes import UserRoutes
from review.routes.review_routes import ReviewRoutes
from review.controllers.review_controller import ReviewController
# from user.controllers.user_controller import UserController

from fastapi_users.authentication import JWTStrategy


origins = [
    "http://localhost:4200",
    "http://localhost:8000",
]


app = FastAPI(title="HeavyReview")


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

rc = ReviewController()
review_routes = ReviewRoutes(rc)

main_api_router = APIRouter()
# main_api_router.include_router(user_routes.router, prefix="/user", tags=["user"])
main_api_router.include_router(review_routes.router, prefix="/review", tags=["review"])
app.include_router(main_api_router, prefix="/api")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
