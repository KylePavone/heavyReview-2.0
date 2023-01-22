from sqlalchemy import Column, Boolean, String, DateTime, Integer, ForeignKey
from database.database import Base
from sqlalchemy.orm import relationship


class Tag(Base):

    __tablename__ = "tag"

    id = Column(Integer, primary_key=True)
    review_id = Column(Integer, ForeignKey("review.id"))
    tag_name = Column(String, unique=True, nullable=False)
