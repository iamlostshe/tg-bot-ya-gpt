'Модуль запуска бота'

import asyncio
from os import getenv

from aiogram import Bot, Dispatcher

from loguru import logger
from dotenv import load_dotenv

from handlers import routers
from utils.db import check_db

async def main() -> None:
    'Основная функция для запуска бота'

    # Проверяем наличае бд
    await check_db()

    # Подключаем файл под логи
    logger.add('log.log')

    # Получаем токен из .env
    load_dotenv()
    TOKEN = getenv("TG_TOKEN")

    # Инициализируем диспетчер и бота
    dp = Dispatcher()
    bot = Bot(token=TOKEN)

    # Подключаем роутеры
    for r in routers:
        logger.info('Include router: {} ...', r.name)
        dp.include_router(r)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
