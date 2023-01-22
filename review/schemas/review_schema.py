import datetime
from pydantic import BaseModel
from typing import List, Union, Optional


class TunedModel(BaseModel):
    class Config:
        """Tells pydantic to convert even non-dict obj to json"""

        orm_mode = True


class CreateReview(TunedModel):
    title: str
    content: str
    images: List = []
    created: datetime.datetime
    likes_count: int


class ShowReview(TunedModel):
    id: int
    title: str
    content: str
    images: List = []
    created: datetime.datetime
    likes_count: int


class UpdateReview(TunedModel):
    title: Optional[str] = None
    content: str
    images: List = []
