'Обработка приветственного сообщения'

from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Router

from utils import db

router = Router(name=__name__)

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    'Хендлер комманды /start'
    await message.answer(f"Привет, {message.from_user.full_name}! Это приветственное сообщение!")

    sourse = message.text[7:]

    user_id = message.from_user.id
    first_name = message.from_user.first_name
    is_premium = message.from_user.is_premium
    language_code = message.from_user.language_code
    last_name = message.from_user.last_name
    username = message.from_user.username

    await db.add_user(
        user_id,
        sourse,
        first_name,
        last_name,
        is_premium,
        language_code,
        username
    )
