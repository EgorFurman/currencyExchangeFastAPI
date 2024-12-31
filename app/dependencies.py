import asyncio
from decimal import Decimal

import app.schemas as schemas
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


#print(
#    asyncio.run(
#        db_service().upd_exchange_rate(
#            schema=schemas.ExchangeRateCodesSchema(base_currency_code='USD', target_currency_code='EUR', rate=Decimal('0.96'))
#    )
#))

#print(
#    asyncio.run(
#        db_service().upd_exchange_rate(
#            schema=schemas.ExchangeRateCodesSchema(base_currency_code='USD', target_currency_code='sdf', rate=Decimal('0.96'))
#        )
#    )
#)

#print(
#    asyncio.run(
#        db_service().get_currency(code='sdf')
#    )
#)

#print(
#    asyncio.run(
#        db_service().get_currencies()
#    )
#)

#print(
#    asyncio.run(
#        db_service().add_currency(schema=schemas.CurrencySchema(code='USD', name='USD', sign='$')),
#    )
#)