import datetime
from sqlalchemy import Column, Integer, Boolean, String, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from sqlalchemy.orm import relationship
from database.database import Base
from models.tag_model import Tag
from models.review_tag_model import review_tag


class Review(Base):

    __tablename__ = "review"

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, nullable=False)
    content = Column(Text, nullable=False)
    updated = Column(DateTime, default=datetime.datetime.now())
    likes_count = Column(Integer, default=0)
    tags = relationship("Tag", secondary="review_tag", back_populates="reviews")

    def __init__(self, *args, **kwargs):
        super(Review, self).__init__(*args, **kwargs)
