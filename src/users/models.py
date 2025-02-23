"""
User model
"""

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.asyncio import AsyncSession

from src import Base, get_db


class User(SQLAlchemyBaseUserTableUUID, Base):
    """
    User model with UUID id column
    """

    __tablename__ = "user"

    full_name: Mapped[str] = mapped_column(String(length=100), nullable=False)
    comments: Mapped[list["Comment"]] = relationship("Comment", back_populates="news")


async def get_user_db(session: AsyncSession = Depends(get_db)):
    yield SQLAlchemyUserDatabase(session, User)


