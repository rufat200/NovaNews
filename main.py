from fastapi import FastAPI

from src.news import categories_router, news_router
from src.users import users_router

app = FastAPI()

app.include_router(router=categories_router)
app.include_router(router=news_router)
app.include_router(router=users_router)