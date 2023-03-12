from sqlalchemy import Column, Boolean, String, DateTime, Integer, ForeignKey, Table
from database.database import Base


review_tag = Table(
    "review_tag",
    Base.metadata,
    Column("review_id", ForeignKey("review.id", ondelete='CASCADE')),
    Column("tag_id", ForeignKey("tag.id", ondelete='CASCADE'))
)