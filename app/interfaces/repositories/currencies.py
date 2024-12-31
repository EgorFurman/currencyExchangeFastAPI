from typing import TypedDict, Type
from abc import ABC, abstractmethod

from sqlalchemy import select, update, delete

from app.interfaces.repositories.base import AbstractRepository
from app.models.currencies import Currencies
import app.schemas as schemas


class AbstractCurrenciesRepository(AbstractRepository[Currencies], ABC):
    _model: Type[Currencies] = Currencies

    @abstractmethod
    async def read_by_code(self, code: str, **kwargs) -> Currencies | None:
        """
        получить объект по коду валюту
        :param code: айди валюты в бд
        :return: Currencies | None - Объект валюты или None
        """
        pass

    #async def read_by_code(self, code: str) -> ModelType | None:
    #    async with self._session() as session:
    #        stmt = select(self._model).where(self._model.code == code)
    #        res = await session.execute(stmt)
    #        return res.scalars().first()



