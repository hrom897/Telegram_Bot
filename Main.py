import logging
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils import executor

# Включаємо логування
logging.basicConfig(level=logging.INFO)

# Твій Telegram ID (заміни на свій)
ADMIN_ID = 7847653716

# Токен бота
bot = Bot(token="7585427991:AAENGj1uCtdUIJhVAwbjRsSWiB4uyiHg7zA")

# Диспетчер
dp = Dispatcher()

# Файл для збереження тексту
DATA_FILE = "data.txt"

# Функція для читання повідомлення
def get_message():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return file.read()
    return "Користувач зараз: Працює 🥰 \nПерерва в: 13:00 💌"

# Функція для збереження повідомлення
def save_message(text):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        file.write(text)

# Хендлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    text = get_message()
    await message.answer(text)

# Хендлер для адміну /admin <текст>
@dp.message(Command("admin"))
async def cmd_admin(message: Message):
    if message.from_user.id == ADMIN_ID:
        new_text = message.text.replace("/admin", "").strip()
        if not new_text:
            await message.reply("❌ Введи новий текст після команди /admin")
            return
        
        save_message(new_text)
        await message.reply("✅ Повідомлення оновлено!")
    else:
        await message.reply("❌ У вас немає прав для цієї команди!")

# Запуск бота
async def main():
    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
