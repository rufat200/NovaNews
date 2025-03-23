from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from src.news import categories_router, news_router, comments_router
from src.users import users_router
from src.media import media_router


app = FastAPI()

app.include_router(router=categories_router)
app.include_router(router=news_router)
app.include_router(router=users_router)
app.include_router(router=comments_router)
app.include_router(router=media_router)

openapi_schema = get_openapi(
        title="FastNews API",
        version="1.0.0",
        description="This is a simple FastAPI project with JWT authentication, SQLAlchemy ORM, and PostgreSQL database, alembic for migrations, and docker-compose for development and production environments.",
        routes=app.routes,
    )
openapi_schema["components"]["securitySchemes"] = {
    "BearerAuth": {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT",
    }
}
for path in openapi_schema["paths"].values():
    for method in path:
        path[method]["security"] = [{"BearerAuth": []}]

app.openapi_schema = openapi_schema