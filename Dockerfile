# Використовуємо Python-образ
FROM python:3.11

# Створюємо робочу директорію
WORKDIR /app

# Копіюємо проєкт
COPY . .

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Запускаємо Django-сервер
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
