from aiogram import Router

from src.handlers.private.user.start import router as start_router
from src.handlers.private.user.weather import router as weather_router

router = Router()

router.include_router(start_router)
router.include_router(weather_router)
