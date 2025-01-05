from app.services.db_service import DBService
import app.exceptions.exceptions as exceptions
import app.schemas as schemas


class ExchangeService:
    def __init__(self, db_service: "DBService"):
        self.db_service = db_service

    async def convert(self, exchange: schemas.ExchangeSchema) -> schemas.ExchangeDetailsSchema:
        try:
            return await self._try_get_direct_convert(exchange)
        except exceptions.ExchangeRateNotFoundError:
            try:
                return await self._try_get_inverse_convert(exchange)
            except exceptions.ExchangeRateNotFoundError:
                try:
                    return await self._try_get_usd_base_convert(exchange)
                except exceptions.ExchangeRateNotFoundError:
                    raise exceptions.ImpossibleConvertError(exchange.base, exchange.target)

    async def _try_get_direct_convert(self, exchange: schemas.ExchangeSchema) -> schemas.ExchangeDetailsSchema:
        exchange_rate = await self.db_service.get_exchange_rate(
            base_code=exchange.base, target_code=exchange.target
        )

        return schemas.ExchangeDetailsSchema(
            base_currency=exchange_rate.base_currency,
            target_currency=exchange_rate.target_currency,
            rate=exchange_rate.rate,
            amount=exchange.amount,
            converted_amount=round(exchange.amount * exchange_rate.rate, 2),
        )

    async def _try_get_inverse_convert(self, exchange: schemas.ExchangeSchema) -> schemas.ExchangeDetailsSchema:
        exchange_rate = await self.db_service.get_exchange_rate(
            base_code=exchange.target, target_code=exchange.base
        )

        return schemas.ExchangeDetailsSchema(
            base_currency=exchange_rate.base_currency,
            target_currency=exchange_rate.target_currency,
            rate=exchange_rate.rate,
            amount=exchange.amount,
            converted_amount=round(exchange.amount * (1 / exchange_rate.rate), 2),
        )

    async def _try_get_usd_base_convert(self, exchange: schemas.ExchangeSchema) -> schemas.ExchangeDetailsSchema:
        usd_to_base_rate = await self.db_service.get_exchange_rate(
            base_code='USD', target_code=exchange.base
        )
        usd_to_target_rate = await self.db_service.get_exchange_rate(
            base_code='USD', target_code=exchange.target
        )

        rate = usd_to_base_rate.rate / usd_to_target_rate.rate

        return schemas.ExchangeDetailsSchema(
            base_currency=usd_to_base_rate.target_currency,
            target_currency=usd_to_target_rate.target_currency,
            rate=rate,
            amount=exchange.amount,
            converted_amount=round(exchange.amount * rate, 2),
        )
