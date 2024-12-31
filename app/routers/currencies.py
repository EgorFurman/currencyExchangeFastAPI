from typing import Annotated

from fastapi import APIRouter, Form, Path, Depends

from app.services import DBService
from app.dependencies import db_service
import app.schemas as schemas

router = APIRouter()


@router.get(
    "/currencies", status_code=200
)
async def get_currencies(
        service: Annotated[DBService, Depends(db_service)],
) -> list[schemas.CurrencyIDSchema]:
    #try:
    return await service.get_currencies()
    #except Exception as e:
    #    print(e)


@router.post(
    "/currencies", status_code=201
)
async def post_currencies(
        currency: Annotated[schemas.CurrencySchema, Form()],
        service: Annotated[DBService, Depends(db_service)],
) -> schemas.CurrencyIDSchema:
    #try:
        #response = await service.add_currency(currency)
        return await service.add_currency(currency)
    #except Exception as e:
    #    print(e)


@router.get("/currency/{code}", status_code=200)
async def get_currency(
        code: Annotated[str, Path(title='The code of the currency to get', min_length=3, max_length=3, example='USD')],
        service: Annotated[DBService, Depends(db_service)],
) -> schemas.CurrencyIDSchema:
    #try:
    return await service.get_currency(code)
    #except Exception as e:
    #    print(e)
