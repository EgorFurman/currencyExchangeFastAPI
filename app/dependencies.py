from app.repositories import CurrenciesRepository, ExchangeRatesRepository
from app.services import DBService
from app.services import ExchangeService


def db_service():
    return DBService(
        currencies_repo=CurrenciesRepository(),
        exchange_rates_repo=ExchangeRatesRepository()
    )


def exchange_service():
    return ExchangeService(
        db_service=db_service()
    )
