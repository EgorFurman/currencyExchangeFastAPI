from decimal import Decimal

from pydantic import Field

from app.schemas.base import BaseSchema
from app.schemas.currencies import CurrencyIDSchema


class ExchangeSchema(BaseSchema):
    base: str = Field(min_length=3, max_length=3)
    target: str = Field(min_length=3, max_length=3)
    amount: Decimal = Field(max_digits=100, decimal_places=6, ge=0)


class ExchangeDetailsSchema(BaseSchema):
    base_currency: "CurrencyIDSchema"
    target_currency: "CurrencyIDSchema"
    rate: Decimal = Field(max_digits=9, decimal_places=6, gt=0)
    amount: Decimal = Field(max_digits=100, decimal_places=6, ge=0)
    converted_amount: Decimal = Field(max_digits=100, decimal_places=6, ge=0)




