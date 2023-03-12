import datetime
from fastapi import HTTPException, Depends
from classy_fastapi import Routable, get, delete, post, put
from review.controllers.review_controller import ReviewController
from review.schemas.review_schema import CreateReview, ShowReview, UpdateReview
from database.database import get_session
from sqlalchemy.exc import IntegrityError



class ReviewRoutes(Routable):

    def __init__(self, rc: ReviewController):
        super().__init__()
        self.__rc = rc


    @post('/create')
    async def create_review(self, body: CreateReview, session=Depends(get_session)):
        await self.__rc.save_review(body, session)
        try:
            await session.commit()
            return {
                "status": 201,
                "message": "Done"
            }
        except Exception:
            await session.rollback()
            raise HTTPException(status_code=500, detail=None)

    @get("/{id}", response_model=ShowReview)
    async def get_review_by_id(self, id: int, session=Depends(get_session)):
        review = await self.__rc.get_review_by_id(id, session)
        if review:
            return ShowReview(
                id=review.id,
                title=review.title,
                content=review.content,
                updated=review.updated,
                likes_count=review.likes_count
            )
        raise HTTPException(status_code=404, detail="Not Found")

    # @post("/update")
    # async def update_review(self, review_id: int, body: UpdateReview, session=Depends(get_session)):
    #     await self.__rc.update_review(review_id, body, session)
    #     try:
    #         await session.commit()
    #         return "Updated"
    #     except IntegrityError:
    #         await session.rollback()
    #         raise HTTPException(status_code=402, detail="Integrity Error!")

    @get("/delete/{id}")
    async def delete_review(self, id: int, session=Depends(get_session)):
        result = await self.__rc.get_review_by_id(id, session)
        if result is None:
            raise HTTPException(status_code=404, detail="Not Found!")
        await self.__rc.delete_review(id, session)
        await session.commit()
        return {
            "status": 204
        }
        

    @get("")
    async def get_all(self, session=Depends(get_session)):
        result = await self.__rc.get_all_info(session)
        # print(result)
        return result


