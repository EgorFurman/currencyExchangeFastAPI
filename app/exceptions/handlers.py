from fastapi import Request, FastAPI
from starlette.responses import JSONResponse

import app.exceptions.exceptions as exceptions


def register_exception_handlers(app: "FastAPI"):
    @app.exception_handler(exceptions.CurrencyNotFoundError)
    async def currency_not_found(request: Request, exc: exceptions.CurrencyNotFoundError):
        return JSONResponse(
            status_code=404,
            content={"message": str(exc)},
        )

    @app.exception_handler(exceptions.ExchangeRateNotFoundError)
    async def exchange_rate_not_found(request: Request, exc: exceptions.ExchangeRateNotFoundError):
        return JSONResponse(
            status_code=404,
            content={"message": str(exc)},
        )

    @app.exception_handler(exceptions.ImpossibleConvertError)
    async def impossible_convert(request: Request, exc: exceptions.ImpossibleConvertError):
        return JSONResponse(
            status_code=404,
            content={"message": str(exc)},
        )

    @app.exception_handler(exceptions.InsertAlreadyExistsCurrencyError)
    async def insert_already_exists_currency(request: Request, exc: exceptions.InsertAlreadyExistsCurrencyError):
        return JSONResponse(
            status_code=409,
            content={"message": str(exc)}
        )

    @app.exception_handler(exceptions.InsertAlreadyExistsExchangeRateError)
    async def insert_already_exists_exchange_rate(request: Request, exc: exceptions.InsertAlreadyExistsExchangeRateError):
        return JSONResponse(
            status_code=409,
            content={"message": str(exc)}
        )

    @app.exception_handler(exceptions.DatabaseAccessError)
    async def database_access_error(request: Request, exc: exceptions.DatabaseAccessError):
        return JSONResponse(
            status_code=500,
            content={"message": str(exc)},
        )