FROM python:3.12-slim

WORKDIR /app/


RUN pip install poetry

# Копирование файлов Poetry (pyproject.toml и poetry.lock)
COPY . /app/

# Установка зависимостей
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi
#
# Команда по умолчанию (может быть переопределена в docker-compose.yml)
CMD ["celery", "-A", "app.celery_main.celery_app", "beat", "--loglevel=info"]