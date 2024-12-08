import asyncio

from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine

from config import settings


engine = create_async_engine(
    url=settings.database_url_asyncpg
)


async def get_123():
    async with engine.connect() as connection:
        res = await connection.execute(text("SELECT VERSION()"))
        print(f'{res.all()}')


asyncio.run(get_123())