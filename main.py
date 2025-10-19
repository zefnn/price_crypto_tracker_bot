import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command

from config import BOT_TOKEN
from bot.handlers import cmd_start, cmd_help, cmd_price, cmd_msg, cmd_list

# Инициализация диспетчера
dp = Dispatcher()

# Регистрация обработчиков
dp.message.register(cmd_start, Command("start"))
dp.message.register(cmd_help, Command("help"))
dp.message.register(cmd_price, Command("price"))
dp.message.register(cmd_list, Command("list"))
dp.message.register(cmd_msg)



async def main() -> None:
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    try:
        # Пропускаем старые сообщения при запуске
        await bot.delete_webhook(drop_pending_updates=True)
        # Запускаем опрос серверов Telegram
        await dp.start_polling(bot)
    finally:
        # Закрываем сессию бота при завершении работы
        await bot.session.close()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())