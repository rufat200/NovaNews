сначала перед запуском проекта, нужно сделать следующее

1. Создай **.env** сделай пароль таким же **123456**
2. Запусти Docker Desktop
3. Пропиши следующее
```bash
docker run --name fast_db -e POSTGRES_PASSWORD=123456 -p 5432:5432 -d postgres
```

```bash
alembic revision --autogenerate -m "впиши сюда любой коммит(тут создаешь миграции с модельками, поэтому давай нормальные названия этим коммитам)"

alembic upgrade head
```

- если новичок то запусти это

```
fastapi dev main.py
```

- если продвинутый то это

```
uvicorn main:app --reload
```

4. Если проблемы с алембиком то удали две папки **alembic.ini** и **alembic**, после пропиши
```bash
alembic init -t async alembic
```
после вернись к 3 действию

5. Для докер компоса

```bash
docker compose up --build -d
```