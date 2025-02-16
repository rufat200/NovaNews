from typing import Sequence

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Category, News
from src import DBManager


class NewsService():
    
    @classmethod
    async def get_news(
        cls,
        db: AsyncSession,
        offset: int=0,
        limit: int=10
    ) -> Sequence[News]:
        return await DBManager.get_objects(db, model=News, offset=offset, limit=limit)
    
    @classmethod
    async def get_news_item(
        cls,
        db: AsyncSession,
        news_id: int
    ) -> News:
        news_item = await DBManager.get_object(db=db, model=News, field="id", value=news_id)
        if not news_item:
            raise HTTPException(status_code=404, detail="News not found")
        return news_item

    @classmethod
    async def create_news_item(
        cls,
        db: AsyncSession,
        news_item: dict
    ) -> News:
        return await DBManager.create_object(**news_item, db=db, model=News, commit=True)
    
    @classmethod
    async def delete_news_item(
        cls,
        db: AsyncSession,
        news_id: int
    ) -> None:
        await DBManager.delete_object(db=db, model=News, field="id", value=news_id, commit=True)
    
    @classmethod
    async def update_news_item(
        cls, 
        db: AsyncSession,
        news_id: int,
        news_item: dict,
        partial: bool=False
    ) -> News:
        if partial:
            news_item = await DBManager.partial_update_object(**news_item, db=db, model=News, field="id", value=news_id, commit=True)
        else:
            news_item = await DBManager.update_object(**news_item, db=db, model=News, field="id", value=news_id, commit=True)


class CategoryService():

    @classmethod
    async def get_categories(
        cls,
        db: AsyncSession,
        offset: int=0,
        limit: int=10
    ) -> Sequence[Category]:
        return await DBManager.get_objects(db, model=Category, offset=offset, limit=limit)

    @classmethod
    async def get_category(
        cls,
        db: AsyncSession,
        category_id: int
    ) -> Category:
        category = await DBManager.get_object(db=db, model=Category, field="id", value=category_id)
        if category is None:
            raise HTTPException(status_code=404, detail="Category not found")
        return category

    @classmethod
    async def create_category(
        cls,
        db: AsyncSession,
        category: dict
    ) -> Category:
        return await DBManager.create_object(**category, db=db, model=Category, commit=True)

    @classmethod
    async def delete_category(
        cls,
        db: AsyncSession,
        category_id: int
    ) -> None:
        await DBManager.delete_object(db=db, model=Category, field="id", value=category_id, commit=True)

    @classmethod
    async def update_category(
        cls,
        db: AsyncSession,
        category_id: int,
        category: dict,
        partial: bool=False
    ) -> Category:
        if partial:
            category = await DBManager.partial_update_object(**category, db=db, model=Category, field="id", value=category_id, commit=True)
        else:
            category = await DBManager.update_object(**category, db=db, model=Category, field="id", value=category_id, commit=True)

        if category is None:
            raise HTTPException(status_code=404, detail="Category not found")
        return category