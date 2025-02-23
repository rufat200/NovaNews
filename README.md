сначала перед запуском проекта, нужно сделать следующее

1. Создай **.env** сделай пароль таким же **123456**
2. Запусти Docker Desktop
3. Пропиши следующее
```bash
docker run --name fast_db -e POSTGRES_PASSWORD=123456 -p 5432:5432 -d postgres

alembic revision --autogenerate -m "ВПИШИ СЮДА ВСЁ ЧТО ЗАХОЧЕШЬ"

alembic upgrade head
```

- елси новичок то запусти это

```
fastapi dev main.py
```

- если продвинутый то это

```
uvicorn main:app --reload
```