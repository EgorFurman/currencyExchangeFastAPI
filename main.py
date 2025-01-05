from fastapi import FastAPI

from app.routers import currencies, exchange_rates, exchanges
from app.middlewares import register_middlewares
from app.exceptions.handlers import register_exception_handlers

app = FastAPI()


app.include_router(currencies.router)
app.include_router(exchange_rates.router)
app.include_router(exchanges.router)


register_exception_handlers(app)
register_middlewares(app)
