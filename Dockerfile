# Используйте официальный образ Python
FROM python:3.12

# Создаем и переходим в рабочую директорию
WORKDIR /app

# Копируем файл requirements.txt
COPY ../requirements.txt .

# Устанавливаем зависимости
#RUN apt-get update \
#    && apt-get install -y build-essential libpq-dev \
#    && pip install --no-cache-dir -r requirements.txt
#
#RUN pip install uvicorn

# Копируем все остальные файлы приложения в контейнер
#COPY . .

RUN pip install --no-cache-dir -r requirements.txt

COPY .. .

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Экспонируем порт, который слушает ваше приложение
EXPOSE 10000

# Команда для запуска вашего приложения
CMD ["/usr/local/bin/uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
