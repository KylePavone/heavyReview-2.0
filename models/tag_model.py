from sqlalchemy import Column, Boolean, String, DateTime, Integer, ForeignKey
from database.database import Base
from sqlalchemy.orm import relationship


class Tag(Base):

    __tablename__ = "tag"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    reviews = relationship("Review", secondary="review_tag", back_populates="tags")
    
    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
