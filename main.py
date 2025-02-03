from fastapi import FastAPI
from pydantic import BaseModel


class News(BaseModel):
    title: str
    content: str | None = None

app = FastAPI()

fake_db = [
    {"news_title": "GHOSTS IS REAL!!!", "news_id": 1},
    {"news_title": "WHO STOLE MY PANTS??", "news_id": 2},
    {"news_title": "AGAIN! THEY DIDN'T RAISE MY SALARY?! AND HOW TO LIVE WITH IT NOW?", "news_id": 3},
    {"news_title": "AMERICA IS DROWNING AGAIN IN DEBT!!!", "news_id": 4},
]


@app.get('/')
async def root():
    return {"message": "Hello world!"}

@app.get("/news/{news_id}")
async def read_news(news_id: int):
    for news in fake_db:
        if news['news_id'] == news_id:
            return news
    return fake_db