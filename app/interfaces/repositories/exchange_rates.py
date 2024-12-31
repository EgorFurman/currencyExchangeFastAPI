from abc import ABC, abstractmethod
from decimal import Decimal
from typing import TypedDict, Type

from sqlalchemy import select, and_, update
from sqlalchemy.orm import joinedload, lazyload, aliased, subqueryload

from app.interfaces.repositories.base import AbstractRepository
from app.models.exchange_rates import ExchangeRates
import app.schemas as schemas


class AbstractExchangeRatesRepository(AbstractRepository[ExchangeRates], ABC):
    _model: Type[ExchangeRates] = ExchangeRates

    @abstractmethod
    async def read_by_currencies_codes(
            self, base_currency_code: str, target_currency_code: str, **kwargs
    ) -> ExchangeRates | None:
        """
        получить обменный рейтинг по кодам валют
        :param base_currency_code: код базовой валюты
        :param target_currency_code: код целевой валюты
        :return: ExchangeRates | None - Объект обменного рейтинга или None
        """

    @abstractmethod
    async def update_rate_by_currencies_codes(
            self, base_currency_code: str, target_currency_code: str, rate: Decimal, **kwargs
    ) -> ExchangeRates:
        """
        обновить обменный рейтинг по кодам валют
        :param base_currency_code: код базовой валюты
        :param target_currency_code: код целевой валюты
        :param rate: курс обмена для обновления
        :return: ExchangeRates - обновленный объект обменного рейтинга или None
        """
#
    #@abstractmethod
    #def update_by_currencies_codes(self, *args, **kwargs):
    #    pass





    # async def read_by_currencies_codes_query(
    #         self, base_currency_code: str, target_currency_code: str, with_currencies: bool = True
    # ):
    #     async with self._session() as session:
    #         rate = await (
    #             session.query(self._model).
    #             options(joinedload(self._model.base_currency), joinedload(self._model.target_currency)).
    #             filter(
    #                 and_(
    #                     self._model.base_currency.code == base_currency_code,
    #                     self._model.target_currency.code == target_currency_code
    #                 )
    #             )
    #         )
#
    #         return rate.all()


    #async def read_by_codes(self, base_currency_code: str, target_currency_code: str):


