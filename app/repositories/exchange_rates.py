from decimal import Decimal

from sqlalchemy import insert, select, update, delete, and_
from sqlalchemy.orm import joinedload

from app.interfaces.repositories.exchange_rates import AbstractExchangeRatesRepository
from app.models.exchange_rates import ExchangeRates


class ExchangeRatesRepository(AbstractExchangeRatesRepository):
    async def create(self, values: dict, **kwargs) -> int:
        async with self._session() as session:
            stmt = insert(self._model).values(**values).returning(self._model.id)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalars().first()

    async def read(self, id: int, with_currencies: bool = True, **kwargs) -> ExchangeRates | None:
        # try:
        async with self._session() as session:
            stmt = select(self._model).where(self._model.id == id)

            if with_currencies:
                stmt = self._with_currencies(stmt)

            res = await session.execute(stmt)
            return res.scalars().first()

    async def read_by_currencies_codes(
            self, base_currency_code: str, target_currency_code: str, with_currencies: bool = True, **kwargs
    ) -> ExchangeRates | None:

        async with self._session() as session:
            stmt = (
                select(self._model).where(
                    and_(
                        self._model.base_currency.has(code=base_currency_code),
                        self._model.target_currency.has(code=target_currency_code)
                    )
                )
            )

            if with_currencies:
                stmt = self._with_currencies(stmt)

            res = await session.execute(stmt)
            return res.scalars().first()

    async def list(self, with_currencies: bool = True, **kwargs) -> list[ExchangeRates]:
        async with self._session() as session:
            stmt = select(self._model)

            if with_currencies:
                stmt = self._with_currencies(stmt)

            res = await session.execute(stmt)
            return res.scalars().all()

    async def update(self, id: int, values: dict, with_currencies: bool = True, **kwargs) -> ExchangeRates:
        pass

    async def update_rate_by_currencies_codes(
            self, base_currency_code: str, target_currency_code: str, rate: Decimal, with_currencies: bool = True, **kwargs
    ) -> ExchangeRates:

        async with self._session() as session:
            stmt = (
                update(self._model).where(
                    and_(
                        self._model.base_currency.has(code=base_currency_code),
                        self._model.target_currency.has(code=target_currency_code)
                    )
                ).values(rate=rate,).returning(self._model)
            )

            if with_currencies:
                stmt = self._with_currencies(stmt)

            res = await session.execute(stmt)
            await session.commit()

            rate = res.scalars().first()
            await session.refresh(rate)

            return rate

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

    def _with_currencies(self, stmt):
        stmt = stmt.options(joinedload(self._model.base_currency), joinedload(self._model.target_currency))
        return stmt

