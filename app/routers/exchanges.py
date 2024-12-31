from typing import Annotated

from fastapi import APIRouter, Query, Depends

from app.services import ExchangeService
from app.dependencies import exchange_service
import app.schemas as schemas


router = APIRouter()


@router.get("/exchange", status_code=200)
async def get_exchange(
        exchange: Annotated[schemas.ExchangeSchema, Query()],
        service: Annotated[ExchangeService, Depends(exchange_service)]
) -> schemas.ExchangeDetailsSchema:

    return await service.convert(exchange)
    #return exchange
