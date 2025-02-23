"""
Pydantic schemas for News
"""

from datetime import datetime

from pydantic import BaseModel

from .categories import CategoryReadSchema
from .comments import CommentReadSchema

class NewsReadSchema(BaseModel):
    """
    News read schema
    """
    id: int
    title: str
    content: str | None = None
    images: list[str | None]
    created: datetime
    updated: datetime
    category_id: int | None = None

    class Config:
        from_attributes = True


class NewsReadDetailsSchema(NewsReadSchema):
    """
    News read schema with detailed category data
    """
    category: CategoryReadSchema | None = None
    comments: list[CommentReadSchema]