'Обработка всех остальных сообщений'

from aiogram.enums.content_type import ContentType
from aiogram.types import Message
from aiogram import F, Router

from loguru import logger

from utils import db
from utils.gpt import gpt

router = Router(name=__name__)

@router.message(F.text)
async def echo_handler(message: Message) -> None:
    'Хендлер всех текстовых сообщений, кроме /start'
    try:
        msg = await message.answer("YandexGPT думает...")
        result = gpt(message.text)
        await msg.edit_text(result)

    #except ОшибкаYandexGPT:
    except Exception as e:
        await message.answer(f'Во время работы скрипта произошла непредвиденная ошибка: {e}')
        logger.error(e)
