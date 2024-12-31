from decimal import Decimal
from typing import Annotated

from fastapi import APIRouter, Form, Depends, Path, Query

from app.services import DBService
from app.dependencies import db_service
import app.schemas as schemas

router = APIRouter()


@router.get("/exchange-rates", status_code=200)
async def get_exchange_rates(
        service: Annotated[DBService, Depends(db_service)],
) -> list[schemas.ExchangeRateDetailsSchema]:

    res = await service.get_exchange_rates()
    return res


@router.post("/exchange-rates", status_code=201)
async def create_exchange_rates(
        exchange_rate: Annotated[schemas.ExchangeRateCodesSchema, Form()],
        service: Annotated[DBService, Depends(db_service)],
) -> schemas.ExchangeRateDetailsSchema:

    return await service.add_exchange_rate(exchange_rate)


@router.get("/exchange-rate/{codes}", status_code=200)
async def get_exchange_rate(
        codes: Annotated[str, Path(title='The currency pair to get', min_length=6, max_length=6, example='USDEUR')],
        service: Annotated[DBService, Depends(db_service)]
) -> schemas.ExchangeRateDetailsSchema:

    base_code, target_code = codes[:3], codes[3:]
    return await service.get_exchange_rate(base_code, target_code)


@router.patch("/exchange-rate/{codes}", status_code=200)
async def update_exchange_rate(
        codes: Annotated[str, Path(title='The currency pair to get', min_length=6, max_length=6, example='USDEUR')],
        rate: Annotated[Decimal, Query(gt=0, example=0.1), Form()],
        service: Annotated[DBService, Depends(db_service)]
) -> schemas.ExchangeRateDetailsSchema:

    base_code, target_code = codes[:3], codes[3:]
    return await service.upd_exchange_rate(schemas.ExchangeRateCodesSchema(
        base_currency_code=base_code, target_currency_code=target_code, rate=rate)
    )


    #return f'{codes}, {rate}'