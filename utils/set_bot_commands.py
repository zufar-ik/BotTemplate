from aiogram import types
from aiogram.types import WebAppInfo




async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Старт бота"),
            types.BotCommand("help", "Помощь"),
        ]
    )
