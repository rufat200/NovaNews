"""
Main frogramm module
"""

from fastapi import FastAPI

from src import category_router, news_router, users_router


app = FastAPI()

app.include_router(router=category_router)
app.include_router(router=news_router)
app.include_router(router=users_router)