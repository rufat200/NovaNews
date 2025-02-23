from typing import Sequence

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src import DBManager
from users.models import User
from ..models import Comment, News


class CommentService:
    @classmethod
    async def get_comments(
        cls,
        db: AsyncSession,
        news_id: int,
        offset: int = 0,
        limit: int = 10,
    ) -> Sequence[Comment]:
        """
        Получить комментарии для конкретной новости.
        """
        return await DBManager.get_objects(
            db=db,
            model=Comment,
            offset=offset,
            limit=limit,
            filter_by={"news_id": news_id}
        )

    @classmethod
    async def get_comment(
        cls,
        db: AsyncSession,
        comment_id: int,
    ) -> Comment:
        """
        Получить конкретный комментарий по ID.
        """
        comment = await DBManager.get_object(
            db,
            Comment,
            "id",
            comment_id
        )
        if not comment:
            raise HTTPException(status_code=404, detail="Comment not found")
        return comment

    @classmethod
    async def create_comment(
        cls,
        db: AsyncSession,
        comment_data: dict,
        user: User
    ) -> Comment:
        # Проверка существования новости
        if not await DBManager.exists(db, News, "id", comment_data["news_id"]):
            raise HTTPException(status_code=404, detail="News not found")

        comment_data["user_id"] = user.id
        return await DBManager.create_object(db, Comment, **comment_data)

    @classmethod
    async def delete_comment(
        cls,
        db: AsyncSession,
        comment_id: int,
        user: User
    ) -> None:
        comment = await cls.get_comment(db, comment_id)
        if comment.user_id != user.id:
            raise HTTPException(status_code=403, detail="Forbidden")
        await DBManager.delete_object(db, Comment, "id", comment_id)

    @classmethod
    async def update_comment(
        cls,
        db: AsyncSession,
        comment_id: int,
        comment_data: dict,
        user: User
    ) -> Comment:
        comment = await cls.get_comment(db, comment_id)
        if comment.user_id != user.id:
            raise HTTPException(status_code=403, detail="Forbidden")
        return await DBManager.update_object(
            db,
            Comment,
            "id",
            comment_id,
            **comment_data
        )

    @classmethod
    async def partial_update_comment(
        cls,
        db: AsyncSession,
        comment_id: int,
        comment_data: dict,
        user: User,
    ) -> Comment:
        """
        Частичное обновление комментария (только если он принадлежит пользователю).
        """
        comment = await DBManager.partial_update_object(
            db=db,
            model=Comment,
            field="id",
            value=comment_id,
            commit=True,
            **comment_data
        )
        if not comment:
            raise HTTPException(status_code=404, detail="Comment not found")

        if comment.user_id != user.id:
            raise HTTPException(status_code=403, detail="You do not have permission to update this comment")

        return comment
