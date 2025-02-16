from typing import Optional, List
from datetime import datetime

from pydantic import BaseModel


class NewsReadSchema(BaseModel):
    id: int
    title: str
    created: datetime

    class Config:
        from_attributes = True
        alias_generator = lambda field_name: field_name.lower()
        extra = "allow"

class NewsReadItemSchema(BaseModel):
    id: int
    title: str
    content: Optional[str] = None
    images: Optional[List[Optional[str]]] = None
    created: datetime
    updated: datetime
    category_id: Optional[int] = None

    class Config:
        from_attributes = True
        alias_generator = lambda field_name: field_name.lower()
        extra = "allow"

class NewsCreateSchema(BaseModel):
    title: str
    content: Optional[str] = None
    images: Optional[List[Optional[str]]] = None
    category_id: Optional[int] = None



class CategoryReadSchema(BaseModel):
    id: int
    name: str
    created: datetime

    class Config:
        from_attributes = True
        alias_generator = lambda field_name: field_name.lower()
        extra = "allow"

class CategoryCreateSchema(BaseModel):
    name: str