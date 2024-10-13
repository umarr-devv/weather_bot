from aiogram import types, Router
from aiogram.filters import CommandStart, CommandObject

router = Router()


@router.message(CommandStart())
async def on_start(message: types.Message, command: CommandObject):
    text = f'👋 Привет, <b>{message.from_user.first_name}</b>!\n' \
           'Я 🤖 бот, который поможет узнать погоду в любом городе.\n' \
           'Просто напишите название города, и я покажу вам текущую погоду. Давайте начнем! ☀️🌧️🌍'
    await message.answer(text=text)
