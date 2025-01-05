import logging

from pydantic import ValidationError
from sqlalchemy.exc import OperationalError, IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError

from app.interfaces.repositories import AbstractCurrenciesRepository, AbstractExchangeRatesRepository
from app.logging_config import setup_logging
import app.exceptions.exceptions as exceptions
import app.schemas as schemas

setup_logging()

logger = logging.getLogger('logger')


class DBService:
    def __init__(
            self,
            currencies_repo: AbstractCurrenciesRepository,
            exchange_rates_repo: AbstractExchangeRatesRepository
    ):
        self._currencies_repo = currencies_repo
        self._exchange_rates_repo = exchange_rates_repo

    async def get_currency(self, code: str) -> schemas.CurrencyIDSchema:
        try:
            logger.debug(f'Getting currency with code {code} from {self._currencies_repo}')
            currency = await self._execute_method(self._currencies_repo.read_by_code, code=code)

            logger.debug(f'Currency with {code} found')
            return schemas.CurrencyIDSchema.model_validate(currency)

        except ValidationError:
            logger.debug(f'Currency with {code} not found')
            raise exceptions.CurrencyNotFoundError(code)

        except Exception as e:
            logger.error(
                f'Error for getting currency: {e} with {code} from {self._currencies_repo}', exc_info=True
            )

    async def get_currencies(self) -> list[schemas.CurrencyIDSchema]:
        try:
            logger.debug(f'Getting currencies from {self._currencies_repo}')
            currencies = await self._execute_method(self._currencies_repo.list)

            logger.debug(f'Currencies from {self._currencies_repo} successfully retrieved')
            return [schemas.CurrencyIDSchema.model_validate(currency) for currency in currencies]
        except Exception as e:
            logger.error(
                f'Error for getting currencies: {e} from {self._currencies_repo}', exc_info=True
            )

    async def add_currency(self, schema: schemas.CurrencySchema) -> schemas.CurrencyIDSchema:
        try:
            logger.debug(f'Adding currency {schema.code} to {self._currencies_repo}')
            id = await self._execute_method(self._currencies_repo.create, values=schema.model_dump())

            logger.debug(f'Currency {schema.code} added to {self._currencies_repo}')
            currency = await self._execute_method(self._currencies_repo.read, id=id)

            return schemas.CurrencyIDSchema.model_validate(currency)
        except IntegrityError:
            logger.debug(f'Currency {schema.code} already exists in {self._currencies_repo}')
            raise exceptions.InsertAlreadyExistsCurrencyError(code=schema.code)
        except Exception as e:
            logger.error(
                f'Error for adding currency: {e} to {self._currencies_repo}',
                exc_info=True
            )

    async def get_exchange_rate(self, base_code: str, target_code: str) -> schemas.ExchangeRateDetailsSchema:
        try:
            logger.debug(f'Getting exchange rate for {base_code} to {target_code}')
            rate = await self._execute_method(
                self._exchange_rates_repo.read_by_currencies_codes,
                base_currency_code=base_code,
                target_currency_code=target_code
            )

            logger.debug(f'Exchange rate for {base_code} to {target_code} found')
            return schemas.ExchangeRateDetailsSchema.model_validate(rate)

        except ValidationError:
            logger.debug(f'Exchange rate for {base_code} to {target_code} not found')
            raise exceptions.ExchangeRateNotFoundError(base_code=base_code, target_code=target_code)

        except Exception as e:
            logger.error(
                f'Error for getting exchange rate: {e} from {self._exchange_rates_repo}',
                exc_info=True
            )

    async def get_exchange_rates(self) -> list[schemas.ExchangeRateDetailsSchema]:
        try:
            logger.debug(f'Getting exchange rates from {self._currencies_repo}')
            exchange_rates = await self._execute_method(self._exchange_rates_repo.list)

            logger.debug(f'Exchange rates from {self._exchange_rates_repo} successfully retrieved')
            return [schemas.ExchangeRateDetailsSchema.model_validate(rate) for rate in exchange_rates]
        except Exception as e:
            logger.error(
                f'Error for getting exchange rates: {e} from {self._exchange_rates_repo}',
                exc_info=True
            )

    async def add_exchange_rate(self, schema: schemas.ExchangeRateCodesSchema) -> schemas.ExchangeRateDetailsSchema:
        try:
            base_currency = await self.get_currency(code=schema.base_currency_code)
            target_currency = await self.get_currency(code=schema.target_currency_code)

            logger.debug(f'Adding exchange rate {schema.base_currency_code} to {schema.target_currency_code} to {self._exchange_rates_repo}')
            id = await self._execute_method(
                self._exchange_rates_repo.create,
                values={
                    'base_currency_id': base_currency.id,
                    'target_currency_id': target_currency.id,
                    'rate': schema.rate
                }
            )

            rate = await self._execute_method(self._exchange_rates_repo.read, id=id)
            logger.debug(f'Exchange rate for {base_currency} to {target_currency} added to {self._exchange_rates_repo}')

            return schemas.ExchangeRateDetailsSchema.model_validate(rate)

        except IntegrityError:
            logger.debug(f'Exchange rate for {schema.base_currency_code} to {schema.target_currency_code} already exists in {self._exchange_rates_repo}')
            raise exceptions.InsertAlreadyExistsExchangeRateError(
                base_code=schema.base_currency_code, target_code=schema.target_currency_code
            )
        except Exception as e:
            logger.error(
                f'Error for adding exchange rate: {e} to {self._exchange_rates_repo}',
                exc_info=True
            )

    async def upd_exchange_rate(self, schema: schemas.ExchangeRateCodesSchema) -> schemas.ExchangeRateDetailsSchema:
        try:
            logger.debug(f'Updating exchange rate {schema.base_currency_code} to {schema.target_currency_code} to {self._exchange_rates_repo}')
            rate = await self._execute_method(
                self._exchange_rates_repo.update_rate_by_currencies_codes,
                base_currency_code=schema.base_currency_code,
                target_currency_code=schema.target_currency_code,
                rate=schema.rate
            )

            logger.debug(f'Exchange rate for {schema.base_currency_code} to {schema.target_currency_code} updated')
            return schemas.ExchangeRateDetailsSchema.model_validate(rate)
        except UnmappedInstanceError:
            logger.debug(f'Error updating exchange rate not found in {self._exchange_rates_repo}')
            raise exceptions.ExchangeRateNotFoundError(schema.base_currency_code, schema.target_currency_code)
        except Exception as e:
            logger.error(
                f'Error for updating exchange rate: {e} to {self._exchange_rates_repo}',
                exc_info=True
            )

    @staticmethod
    async def _execute_method(method: callable, **kwargs):
        try:
            return await method(**kwargs)
        except OperationalError as e:
            raise exceptions.DatabaseAccessError(e)
