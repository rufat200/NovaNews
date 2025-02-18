from typing import Sequence

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Category, News
from .services import CategoryService, NewsService
from .schemas import (
    CategoryCreateSchema,
    CategoryReadSchema,
    NewsCreateSchema,
    NewsReadItemSchema,
    NewsReadSchema,
)
from src import get_db


categories_router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

news_router = APIRouter(
    prefix="/news", 
    tags=["News"]
)


@news_router.get("", response_model=Sequence[NewsReadSchema])
async def get_news(offset: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)) -> Sequence[News]:
    return await NewsService.get_news(db, offset, limit)

@news_router.get("/{news_id}", response_model=NewsReadItemSchema)
async def get_news_item(news_id: int, db: AsyncSession = Depends(get_db)) -> News:
    return await NewsService.get_news_item(db, news_id)

@news_router.post("", response_model=NewsReadItemSchema)
async def create_news_item(news_item: NewsCreateSchema, db: AsyncSession = Depends(get_db)) -> News:
    return await NewsService.create_news_item(db, news_item.dict())

@news_router.delete("/{news_id}")
async def delete_news_item(news_id: int, db: AsyncSession = Depends(get_db)) -> None:
    return await NewsService.delete_news_item(db, news_id)

@news_router.put("/{news_id}", response_model=NewsReadItemSchema)
async def update_news_item(news_id: int, news_item: NewsCreateSchema, db: AsyncSession = Depends(get_db)) -> News:
    return await NewsService.update_news_item(db, news_id, news_item.dict())

@news_router.patch("/{news_id}", response_model=NewsReadItemSchema)
async def partial_update_news_item(news_id: int, news_item: NewsCreateSchema, db: AsyncSession = Depends(get_db)) -> News:
    return await NewsService.update_news_item(db, news_id, news_item.dict(), partial=True)



@categories_router.get("", response_model=Sequence[CategoryReadSchema])
async def get_categories(offset: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)) -> Sequence[Category]:
    return await CategoryService.get_categories(db, offset, limit)

@categories_router.get("/{category_id}", response_model=CategoryReadSchema)
async def get_category(category_id: int, db: AsyncSession = Depends(get_db)) -> Category:
    return await CategoryService.get_category(db, category_id)

@categories_router.post("", response_model=CategoryReadSchema)
async def create_category(category: CategoryCreateSchema, db: AsyncSession = Depends(get_db)) -> Category:
    return await CategoryService.create_category(db, category.dict())

@categories_router.delete("/{category_id}")
async def delete_category(category_id: int, db: AsyncSession = Depends(get_db)) -> None:
    return await CategoryService.delete_category(db, category_id)

@categories_router.put("/{category_id}", response_model=CategoryReadSchema)
async def update_category(category_id: int, category: CategoryCreateSchema, db: AsyncSession = Depends(get_db)) -> Category:
    return await CategoryService.update_category(db, category_id, category.dict())

@categories_router.patch("/{category_id}", response_model=CategoryReadSchema)
async def partial_update_category(category_id: int, category: CategoryCreateSchema, db: AsyncSession = Depends(get_db)) -> Category:
    return await CategoryService.update_category(db, category_id, category.dict(), partial=True)
