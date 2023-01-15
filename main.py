from fastapi import FastAPI
import uvicorn
from fastapi.routing import APIRouter
from user.routes.user_routes import UserRoutes
from user.controllers.user_controller import UserController
from database.database import async_session


app = FastAPI(title="HeavyReview")


uc = UserController(async_session)
user_routes = UserRoutes(uc)


main_api_router = APIRouter()
main_api_router.include_router(user_routes.router, prefix="/user", tags=["user"])
app.include_router(main_api_router, prefix="/api")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
