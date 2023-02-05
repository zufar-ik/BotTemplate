import logging

from aiogram import Dispatcher
from data.config import ADMINS


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            try:
                await dp.bot.send_message(admin, "Бот запущен")
            except:
                pass
        except Exception as err:
            logging.exception(err)
