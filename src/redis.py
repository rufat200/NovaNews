import random
import string

from redis import asyncio as aioredis

from src import REDIS_URL

redis_client = aioredis.from_url(url=REDIS_URL)

def generate_verification_code(lenght: int=6) -> str:
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=lenght))