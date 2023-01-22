from fastapi import HTTPException, Depends
from classy_fastapi import Routable, get, delete, post, put
from review.controllers.review_controller import ReviewController
from review.schemas.review_schema import CreateReview, ShowReview, UpdateReview
from database.database import get_session
from sqlalchemy.exc import IntegrityError
from auth.source import current_active_user
from models.user_model import User


class ReviewRoutes(Routable):

    def __init__(self, rc: ReviewController, ):
        super().__init__()
        self.__rc = rc

    @post('/create', response_model=ShowReview)
    async def create_user(self, body: CreateReview, session=Depends(get_session)):
        review = await self.__rc.create_review(body, session)
        try:
            await session.commit()
            return ShowReview(
                id=review.id,
                title=review.title,
                content=review.content,
                images=review.images,
                created=review.created,
                likes_count=review.likes_count
            )
        except IntegrityError:
            await session.rollback()
            raise HTTPException(status_code=402, detail="Email already exists!")

    @get("/{id}", response_model=ShowReview)
    async def get_review_by_id(self, review_id: int, session=Depends(get_session)):
        review = await self.__rc.get_review_by_id(review_id, session)
        if review:
            return ShowReview(
                id=review.id,
                title=review.title,
                content=review.content,
                images=review.images,
                created=review.created,
                likes_count=review.likes_count
            )
        raise HTTPException(status_code=404, detail="Not Found")

    @put("/update")
    async def update_review(self, review_id: int, body: UpdateReview, session=Depends(get_session),
                            user: User = Depends(current_active_user)):
        await self.__rc.update_review(review_id, body, session)
        try:
            await session.commit()
            return "Updated"
        except IntegrityError:
            await session.rollback()
            raise HTTPException(status_code=402, detail="Email already exists!")

    @delete("/delete")
    async def delete_review(self, review_id: int, session=Depends(get_session),
                            user: User = Depends(current_active_user)):
        result = await self.__rc.get_review_by_id(review_id, session)
        if result is None:
            raise HTTPException(status_code=404, detail="Not Found!")
        await self.__rc.delete_review(review_id, session)
        await session.commit()
        return {
            "status": 204
        }

    @get("")
    async def get_all(self, session=Depends(get_session)):
        result = await self.__rc.get_all_info(session)
        return result


