import logging

from fastapi import FastAPI, Request, Response
import uvicorn

from app.routers import currencies, exchange_rates, exchanges
from app.exceptions.handlers import register_exception_handlers


#setup_logging()
#logger = logging.getLogger('logger')
#
## logger.debug("This is a DEBUG message.")
## logger.info("This is an INFO message.")
## logger.warning("This is a WARNING message.")
## logger.error("This is an ERROR message.")
## logger.critical("This is a CRITICAL message.")
#
#print(logger.handlers)
#for handler in logger.handlers:
#    print(f'Handler: {handler}, Level: {handler.level}, Formatter: {handler.formatter}')
app = FastAPI()


app.include_router(currencies.router)
app.include_router(exchange_rates.router)
app.include_router(exchanges.router)


register_exception_handlers(app)
#
#
#@app.get("/")
#def home():
#    return 'Hello World'
#
#
if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, host='0.0.0.0', port=8000)
