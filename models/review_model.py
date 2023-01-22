import datetime
from sqlalchemy import Column, Integer, Boolean, String, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from sqlalchemy.orm import relationship
from database.database import Base
from models.tag_model import Tag


class Review(Base):

    __tablename__ = "review"

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, nullable=False)
    content = Column(Text, nullable=False)
    images = Column(ARRAY(String))
    created = Column(DateTime, default=datetime.datetime.now())
    likes_count = Column(Integer, default=0)
    tags = relationship("Tag")

    def __init__(self, *args, **kwargs):
        super(Review, self).__init__(*args, **kwargs)
