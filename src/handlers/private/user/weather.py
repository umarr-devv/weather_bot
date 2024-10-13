from aiogram import types, Router, Bot, F
from aiogram.utils.chat_action import ChatActionSender

from src.config import Config
from src.service.weather_api import WeatherAPIClient

router = Router()


@router.message(F.content_type == types.ContentType.TEXT)
async def on_weather(message: types.Message, bot: Bot, config: Config):
    async with ChatActionSender.typing(chat_id=message.chat.id, bot=bot):
        data = await WeatherAPIClient.get_weather_by_city(config.weather_api.key, message.text)

        if data:
            weather_emoji = WeatherAPIClient.get_weather_emoji(data['weather'][0]['icon'])
            text = f'🏙 <b>Город</b>: {message.text}\n\n' \
                   f'{weather_emoji} <b>Погода</b>: {data["weather"][0]["main"]}\n' \
                   f'📒 <b>Описание</b>: {data["weather"][0]["description"]}\n\n' \
                   f'🌡️ <b>Температура</b>: <code>{data["main"]["temp"]}°C</code>\n' \
                   f'   ⬆️ <i>Макс</i>: <code>{data["main"]["temp_max"]}°C</code>\n' \
                   f'   ⬇️ <i>Мин</i>: <code>{data["main"]["temp_min"]}°C</code>\n\n' \
                   f'💨 <b>Скорость ветра</b>: <code>{data["wind"]["speed"]} м/c</code>'

            await message.answer(text)
            return
        
        text = '❌ Город с таким названием не найден'
        await message.answer(text)
