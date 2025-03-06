from pydantic import BaseModel

from celery.app import Celery

from .environs import REDIS_URL, BASE_URL


celery_app = Celery("task", broker=REDIS_URL, backend=REDIS_URL)


class TaskStatus(BaseModel):
    id: str
    status: str


@celery_app.task(name="task.print_user_data")
def print_user_data(user: dict) -> bool:
    for key, value in user.items():
        print(f"{key}: {value}")
    return True