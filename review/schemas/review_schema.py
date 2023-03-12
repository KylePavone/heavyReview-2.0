import datetime
from pydantic import BaseModel
from typing import List, Union, Optional


class TunedModel(BaseModel):
    class Config:
        """Tells pydantic to convert even non-dict obj to json"""

        orm_mode = True


class CreateReview(TunedModel):
    id: Optional[int] = None
    title: str
    content: str
    likes_count: Optional[int] = None
    tags: List = []
    

class ShowReview(TunedModel):
    id: int
    title: str
    content: str
    images: List = []
    updated: datetime.datetime
    likes_count: int
    tags: List = []


class UpdateReview(TunedModel):
    title: Optional[str] = None
    content: str
    tags: List = []
    updated: str
