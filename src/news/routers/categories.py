"""
Categories Router
"""

from typing import Sequence, Annotated

from fastapi import APIRouter, Depends, Form
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import Category
from ..schemas import CategoryReadSchema
from ..services import CategoryService
from src import get_db


router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)


@router.get("", response_model=Sequence[CategoryReadSchema])
async def get_categories(
    offset: int = 0, 
    limit:  int = 10, 
    db:     AsyncSession = Depends(get_db)
) -> Sequence[Category]:
    """
    Get all categories
    """
    return await CategoryService.get_categories(
        db=db, 
        offset=offset, 
        limit=limit
    )


@router.get("/{category_id}", response_model=CategoryReadSchema)
async def get_category(
    category_id: int, 
    db:          AsyncSession = Depends(get_db)
) -> Category:
    """
    Get category by id
    """
    return await CategoryService.get_category(
        db=db, 
        category_id=category_id
    )


@router.post("", response_model=CategoryReadSchema)
async def create_category(
    name: Annotated[str | None, Form()] = None,
    db:   AsyncSession = Depends(get_db)
) -> Category:
    """
    Create category
    """
    return await CategoryService.create_category(
        db=db, 
        category={
            "name": name
        }
    )


@router.delete("/{category_id}", status_code=204)
async def delete_category(
    category_id: int, 
    db:          AsyncSession = Depends(get_db)
) -> None:
    """
    Delete category by id
    """
    return await CategoryService.delete_category(
        db=db, 
        category_id=category_id
    )


@router.put("/{category_id}", response_model=CategoryReadSchema)
async def update_category(
    category_id: int,
    name:        Annotated[str, Form()],
    db:          AsyncSession = Depends(get_db)
) -> Category:
    """
    Update category by id
    """
    return await CategoryService.update_category(
        db=db, 
        category_id=category_id, 
        category={
            "name": name
        }
    )


@router.patch("/{category_id}", response_model=CategoryReadSchema)
async def partial_update_category(
    category_id: int, 
    name:        Annotated[str | None, Form()] = None, 
    db:          AsyncSession = Depends(get_db)
) -> Category:
    """
    Update category by id
    """
    return await CategoryService.update_category(
        db=db, 
        category_id=category_id, 
        category={
            "name": name
        }, 
        partial=True
    )
