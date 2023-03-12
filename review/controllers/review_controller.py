from datetime import datetime
from sqlalchemy import select, delete, update, insert
from models.review_model import Review
from database.database import AsyncSession
from models.tag_model import Tag


class ReviewController:
    async def save_review(self, body, session: AsyncSession):
        if body.id:
            return await session.execute(update(Review).values(
                {
                    "title": body.title,
                    "content": body.content,
                    "updated": datetime.now()
                }
            ).where(Review.id == body.id))
        else: 
            review = Review(title=body.title, content=body.content, likes_count=body.likes_count)
            for tag_name in body.tags:
                tag_in_db = await session.execute(select(Tag).where(Tag.name == tag_name))
                if tag_in_db:
                    review.tags.append(tag_in_db.scalars().first())
                else:                
                    tag = Tag(name=tag_name)
                    session.add(tag)
                    review.tags.append(tag)
            session.add(review)
            return review


    async def get_review_by_id(self, review_id: int, session: AsyncSession):
        review = await session.execute(
            select(
                Review.id, Review.title, Review.content, Review.updated, Review.likes_count)
            .where(Review.id == review_id)
        )
        return review.first()

    async def get_all_info(self, session: AsyncSession):
        # result = await session.execute('SELECT * FROM review JOIN review_tag ON review.id = review_tag.review_id JOIN '
        #                                'tag ON tag.id = review_tag.tag_id')
        result = await session.execute('SELECT * FROM review ORDER BY updated DESC;')
        return result.all()
    
    async def delete_review(self, id, session: AsyncSession):
        await session.execute(delete(Review).where(Review.id == id))




