class CurrencyExchangeError(Exception):
    """Base class for exceptions in this project."""
    def __init__(self, *args):
        self.message = 'Base Currency Exchange error.'

    def __str__(self):
        return self.message


class DatabaseAccessError(CurrencyExchangeError):
    """Exception raised when there is an error accessing the database."""
    def __init__(self, error, *args):
        self.message = f'Database access error "{error}"'


class RecordNotFoundError(CurrencyExchangeError):
    """Exception raised when record with the specified parameters not found."""
    def __init__(self, *args):
        self.message = f'Record not found.'


class CurrencyNotFoundError(RecordNotFoundError):
    """Exception raised when currency with the specified parameters not found."""
    def __init__(self, code, *args):
        self.message = f'Currency with code = {code} not found.'


class ExchangeRateNotFoundError(RecordNotFoundError):
    """Exception raised when exchange rate with the specified parameters not found."""

    def __init__(self, base_code, target_code, *args):
        self.message = f'Exchange rate for {base_code} to {target_code} not found.'


class InsertAlreadyExistsRecordError(CurrencyExchangeError):
    """Exception raised when a record already exists."""
    def __init__(self, *args):
        self.message = f'Record already exists.'


class InsertAlreadyExistsCurrencyError(CurrencyExchangeError):
    def __init__(self, code, *args):
        self.message = f'Currency with {code} code already exists.'


class InsertAlreadyExistsExchangeRateError(CurrencyExchangeError):
    def __init__(self, base_code, target_code, *args):
        self.message = f'Exchange rate for currency pair {base_code} to {target_code} already exists.'


class CurrenciesNotExistsError(CurrencyExchangeError):
    """Exception raised when currency(one or both) do not exist."""
    def __init__(self, base_currency, target_currency, *args):
        self.message = f'One or both currencies ({base_currency}, {target_currency}) do not exist in database.'


class MissingCurrencyCodeError(CurrencyExchangeError):
    """Exception raised when missed a currency code."""
    def __init__(self, *args):
        self.message = f'''Currency code('s) is missing.'''


class MissingFieldError(CurrencyExchangeError):
    """Exception raised when a required field is missing."""
    def __init__(self, fields, *args):
        self.message = f'Missing at least one required field: {fields}.'


class BadURLError(CurrencyExchangeError):
    """Exception raised when a URL not found at Server."""
    def __init__(self, url, *args):
        self.message = f'Requested URL: {url} not found at Server'


class ImpossibleConvertError(CurrencyExchangeError):
    """Exception raised when a currency conversion is not possible."""
    def __init__(self, base_code: str, target_code: str, *args):
        self.message = f'Impossible convert {base_code} to {target_code}.'
