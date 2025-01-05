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
		SERVER_IP = 0.0.0.0 # 0.0.0.0 для разработки(localhost). Для развертывания ip удаленного серва
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

## Стек
- Python 3.12
- FastAPI 0.115.6
- PostgreSQL
- Docker
- SQLAlchemy
- Pydantic
- Poetry