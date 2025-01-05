from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from app.config import db_settings


class Base(DeclarativeBase):
    pass


engine = create_async_engine(
    url=db_settings.database_url,
)


session_factory = async_sessionmaker(
    bind=engine,
    # expire_on_commit=False
)
