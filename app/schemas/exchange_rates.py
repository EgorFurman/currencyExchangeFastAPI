from decimal import Decimal

from pydantic import Field, PositiveInt

from app.schemas.base import BaseSchema
from app.schemas.currencies import CurrencyIDSchema


class ExchangeRateIDSchema(BaseSchema):
    base_currency_id: PositiveInt
    quote_currency_id: PositiveInt
    rate: Decimal = Field(max_digits=9, decimal_places=6, gt=0)


class ExchangeRateCodesSchema(BaseSchema):
    base_currency_code: str = Field(min_length=3, max_length=3)
    target_currency_code: str = Field(min_length=3, max_length=3)
    rate: Decimal = Field(max_digits=9, decimal_places=6, gt=0)


class ExchangeRateDetailsSchema(BaseSchema):
    id: PositiveInt
    base_currency: "CurrencyIDSchema"
    target_currency: "CurrencyIDSchema"
    rate: Decimal = Field(max_digits=9, decimal_places=6, gt=0)
