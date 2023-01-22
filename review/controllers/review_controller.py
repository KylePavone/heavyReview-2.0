from sqlalchemy import select, delete, update, insert
from models.review_model import Review
from database.database import AsyncSession
from models.tag_model import Tag


class ReviewController:

    async def create_review(self, body, session: AsyncSession):
        review = Review(title=body.title, content=body.content, images=body.images)
        session.add(review)
        return review

    async def get_review_by_id(self, review_id: int, session: AsyncSession):
        review = await session.execute(
            select(
                Review.id, Review.title, Review.content, Review.images, Review.created, Review.likes_count)
            .where(Review.id == review_id)
        )
        return review.first()

    async def update_review(self, review_id: int, body, session: AsyncSession):
        return await session.execute(update(Review).values(
            {
                "title": body.title,
                "content": body.title,
                "images": body.images
            }
        ).where(Review.id == review_id))

    async def delete_review(self, review_id, session: AsyncSession):
        await session.execute(delete(Review).where(Review.id == review_id))

    async def get_all_info(self, session: AsyncSession):
        result = await session.execute('SELECT * FROM review JOIN tag ON review.id = tag.review_id')
        return result.all()



























