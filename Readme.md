# Проект “Обмен валют”

REST API для описания валют и обменных курсов. Позволяет просматривать и редактировать списки валют и обменных курсов, и совершать расчёт конвертации произвольных сумм из одной валюты в другую.

[Тз проекта](https://zhukovsd.github.io/python-backend-learning-course/projects/currency-exchange/).


## Установка и запуск

1. Склонируйте репозиторий:
    
    ```shell
    git clone https://github.com/EgorFurman/currencyExchangeFastAPI.git
    ```
    
2. Установите Docker:  
	- [Инструкции по установке Docker](https://docs.docker.com/desktop/)

3. Сконфигурируйте `.env` в соответствие с примером
	```
		# Конфигурация базы данных
		POSTGRES_DB = currency_exchange # Имя БД
		POSTGRES_USER = postgres # Имя пользователя БД
		POSTGRES_PASSWORD = 1234 # Пароль пользователя БД
		POSTGRES_HOST = db # Имя контейнера БД. По умолчанию db
		POSTGRES_PORT = 5432 # Порт БД
		
		# Конфигурация сервера
		SERVER_IP = 0.0.0.0 # 0.0.0.0 для разработки(localhost). Для развертывания ip удаленного сервера
	```

4. Запустите проект:
	- **Для dev версии проекта**
	    ```shell
	     docker-compose -f docker-compose.dev.yml up -d --build
	    ```
	- **Для prod версии проекта**
	    ```shell
	     docker-compose -f docker-compose.prod.yml up -d --build
	    ```

## REST API

### Валюты

#### GET `/currencies`

Получение списка валют. Пример ответа:

```
[
    {
        "id": 0,
        "name": "United States dollar",
        "code": "USD",
        "sign": "$"
    },   
    {
        "id": 0,
        "name": "Euro",
        "code": "EUR",
        "sign": "€"
    }
]
```

HTTP коды ответов:

- Успех - 200
- Ошибка (например, база данных недоступна) - 500

#### GET `/currency/EUR`

Получение конкретной валюты. Пример ответа:

```
{
    "id": 0,
    "name": "Euro",
    "code": "EUR",
    "sign": "€"
}
```

HTTP коды ответов:

- Успех - 200
- Код валюты отсутствует в адресе - 400
- Валюта не найдена - 404
- Ошибка (например, база данных недоступна) - 500

#### POST `/currencies`

Добавление новой валюты в базу. Данные передаются в теле запроса в виде полей формы (`x-www-form-urlencoded`). Поля формы - `name`, `code`, `sign`. Пример ответа - JSON представление вставленной в базу записи, включая её ID:

```
{
    "id": 0,
    "name": "Euro",
    "code": "EUR",
    "sign": "€"
}
```

HTTP коды ответов:

- Успех - 200
- Отсутствует нужное поле формы - 400
- Валюта с таким кодом уже существует - 409
- Ошибка (например, база данных недоступна) - 500

### Обменные курсы

#### GET `/exchange_rates`

Получение списка всех обменных курсов. Пример ответа:

```
[
    {
        "id": 0,
        "base_currency": {
            "id": 0,
            "name": "United States dollar",
            "code": "USD",
            "sign": "$"
        },
        "target_currency": {
            "id": 1,
            "name": "Euro",
            "code": "EUR",
            "sign": "€"
        },
        "rate": 0.99
    }
]
```

HTTP коды ответов:

- Успех - 200
- Ошибка (например, база данных недоступна) - 500

#### GET `/exchange_rate/USDRUB`

Получение конкретного обменного курса. Валютная пара задаётся идущими подряд кодами валют в адресе запроса. Пример ответа:

```
{
    "id": 0,
    "base_currency": {
        "id": 0,
        "name": "United States dollar",
        "code": "USD",
        "sign": "$"
    },
    "target_currency": {
        "id": 1,
        "name": "Euro",
        "code": "EUR",
        "sign": "€"
    },
    "rate": 0.99
}

```

HTTP коды ответов:

- Успех - 200
- Коды валют пары отсутствуют в адресе - 400
- Обменный курс для пары не найден - 404
- Ошибка (например, база данных недоступна) - 500

#### POST `/exchange_rates`

Добавление нового обменного курса в базу. Данные передаются в теле запроса в виде полей формы (`x-www-form-urlencoded`). Поля формы - `baseCurrencyCode`, `targetCurrencyCode`, `rate`. Пример полей формы:

- `base_currency_code` - USD
- `target_currency_code` - EUR
- `rate` - 0.99

Пример ответа - JSON представление вставленной в базу записи, включая её ID:

```
{
    "id": 0,
    "base_currency": {
        "id": 0,
        "name": "United States dollar",
        "code": "USD",
        "sign": "$"
    },
    "target_currency": {
        "id": 1,
        "name": "Euro",
        "code": "EUR",
        "sign": "€"
    },
    "rate": 0.99
}
```

HTTP коды ответов:

- Успех - 200
- Отсутствует нужное поле формы - 400
- Валютная пара с таким кодом уже существует - 409
- Одна (или обе) валюта из валютной пары не существует в БД - 404
- Ошибка (например, база данных недоступна) - 500

#### PATCH `/exchange_rate/USDRUB`

Обновление существующего в базе обменного курса. Валютная пара задаётся идущими подряд кодами валют в адресе запроса. Данные передаются в теле запроса в виде полей формы (`x-www-form-urlencoded`). Единственное поле формы - `rate`.

Пример ответа - JSON представление обновлённой записи в базе данных, включая её ID:

```
{
    "id": 0,
    "base_currency": {
        "id": 0,
        "name": "United States dollar",
        "code": "USD",
        "sign": "$"
    },
    "target_currency": {
        "id": 1,
        "name": "Euro",
        "code": "EUR",
        "sign": "€"
    },
    "rate": 0.99
}

```

HTTP коды ответов:

- Успех - 200
- Отсутствует нужное поле формы - 400
- Валютная пара отсутствует в базе данных - 404
- Ошибка (например, база данных недоступна) - 500

### Обмен валюты

#### GET `/exchange?base=BASE_CURRENCY_CODE&target=TARGET_CURRENCY_CODE&amount=$AMOUNT`

Расчёт перевода определённого количества средств из одной валюты в другую. Пример запроса - GET `/exchange?from=USD&to=AUD&amount=10`.

Пример ответа:

```
{
    "base_currency": {
        "id": 0,
        "name": "United States dollar",
        "code": "USD",
        "sign": "$"
    },
    "target_currency": {
        "id": 1,
        "name": "Australian dollar",
        "code": "AUD",
        "sign": "A€"
    },
    "rate": 1.45,
    "amount": 10.00
    "converted_amount": 14.50
}
```

Для всех запросов, в случае ошибки, ответ может выглядеть так:

```json
{
    "message": "Валюта не найдена"
}
```
## Стек
- Python 3.12
- FastAPI 0.115.6
- PostgreSQL
- Docker
- SQLAlchemy
- Pydantic
- Poetry