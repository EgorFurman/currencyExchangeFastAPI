from pydantic import Field, PositiveInt

from app.schemas.base import BaseSchema


class CurrencySchema(BaseSchema):
    code: str = Field(min_length=3, max_length=3)
    name: str = Field(max_length=36)
    sign: str = Field(min_length=1, max_length=3)


class CurrencyIDSchema(CurrencySchema):
    id: PositiveInt
