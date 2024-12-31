from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Type, Mapping, TypedDict

from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from app.database import Base, session_factory
from app.schemas import BaseSchema


ModelType = TypeVar('ModelType', bound=Base)


class AbstractRepository(Generic[ModelType], ABC):
    _session: async_sessionmaker = session_factory

    @property
    @abstractmethod
    def _model(self) -> ModelType:
        """
        Возвращает класс модели SQLAlchemy, связанный с репозиторием
        """

    @abstractmethod
    async def create(self, values: dict, **kwargs) -> int:
        """
        Создать новый объект
        :param values: словарь с ключами дублирующими поля модели и значениями для записи в поля
        :return: int - айди объекта созданного в бд
        """

    @abstractmethod
    async def read(self, id: int, **kwargs) -> ModelType | None:
        """
        получить объект по ID
        :param id: айди объекта в бд
        :return: ModelType | None - объект или None
        """

    @abstractmethod
    async def list(self, **kwargs) -> list[ModelType]:
        """
        получить список объектов
        :return: list[ModelType] - список объектов
        """

    @abstractmethod
    async def update(self, id, values: dict, **kwargs) -> ModelType:
        """
        обновить существующий объект
        :param values: словарь с ключами дублирующими поля модели и значениями для записи в поля
        :return: ModelType - обновленный объект
        """

    @abstractmethod
    async def delete(self, id: int, **kwargs) -> None:
        """
        удалить объект по ID
        :param id: айди объекта в бд
        :return: None
        """

    @abstractmethod
    async def delete_all(self, **kwargs) -> None:
        """
        удалить все объекты из бд
        :param kwargs:
        :return: None
        """


#    async def create(self, schema: BaseSchema) -> ModelType:
#        async with self._session() as session:
#            model = self._model(**schema.model_dump())
#            session.add(model)
#            #stmt = insert(self._model).values(**values).returning(self._model)
#            #res = await session.execute(stmt)
#            await session.commit()
#            await session.refresh(model)
#            return model
#
#    async def read(self, id: int) -> ModelType | None:
#        async with self._session() as session:
#            stmt = select(self._model).where(self._model.id == id)
#            res = await session.execute(stmt)
#            return res.scalars().first()
#
#    async def list(self) -> list[ModelType]:
#        async with self._session() as session:
#            stmt = select(self._model)
#            res = await session.execute(stmt)
#            return res.scalars().all()
#
#    async def update(self, id: int, values: dict) -> ModelType:
#        async with self._session() as session:
#            stmt = update(self._model).where(self._model.id == id).values(**values).returning(self._model)
#            res = await session.execute(stmt)
#            await session.commit()
#            return res.scalars().first()
#
#    async def delete(self, id: int) -> None:
#        async with self._session() as session:
#            stmt = delete(self._model).where(self._model.id == id)
#            await session.execute(stmt)
#            await session.commit()
#