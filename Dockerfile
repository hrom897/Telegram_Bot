# Використовуємо офіційний образ Python
FROM python:3.10

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо файли проєкту
COPY . .

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Запускаємо Telegram-бота
CMD ["python", "Main.py"]
