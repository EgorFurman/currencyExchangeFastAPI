# Используем Python на Alpine
FROM python:3.12.2-alpine

# Отключаем кеширование bytecode и буферизацию вывода
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Отключаем виртуальное окружение Poetry
ENV POETRY_VIRTUALENVS_CREATE=false

# Устанавливаем базовые зависимости
RUN apk update && apk add --no-cache gcc musl-dev postgresql-dev

# Устанавливаем Poetry
RUN pip install --no-cache-dir poetry

# Рабочая директория
WORKDIR /app

# Копируем только файлы для установки зависимостей
COPY pyproject.toml poetry.lock /app/

# Устанавливаем зависимости, исключая dev
RUN poetry install --no-dev

# Копируем весь код
COPY . /app


# Запускаем приложение
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
