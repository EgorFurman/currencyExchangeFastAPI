import asyncio

from sqlalchemy import insert, select, update, delete

from app.interfaces.repositories.currencies import AbstractCurrenciesRepository
from app.models.currencies import Currencies


class CurrenciesRepository(AbstractCurrenciesRepository):
    async def create(self, values: dict, **kwargs) -> int:
        async with self._session() as session:
            stmt = insert(self._model).values(**values).returning(self._model.id)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalars().first()
    
    async def read(self, id: int, **kwargs) -> Currencies | None:
        async with self._session() as session:
            stmt = select(self._model).where(self._model.id == id)
            res = await session.execute(stmt)
            return res.scalars().first()

    async def read_by_code(self, code: str, **kwargs) -> Currencies | None:
        async with self._session() as session:
            stmt = select(self._model).where(self._model.code == code)
            res = await session.execute(stmt)
            return res.scalars().first()

    async def list(self, **kwargs) -> list[Currencies]:
        async with self._session() as session:
            stmt = select(self._model)
            res = await session.execute(stmt)
            return res.scalars().all()

    async def update(self, id: int, values: dict, **kwargs) -> Currencies:
        pass

    async def delete(self, id: int, **kwargs) -> None:
        async with self._session() as session:
            stmt = delete(self._model).where(self._model.id == id)
            await session.execute(stmt)
            await session.commit()

    async def delete_all(self, **kwargs) -> None:
        async with self._session() as session:
            stmt = delete(self._model)
            await session.execute(stmt)
            await session.commit()
