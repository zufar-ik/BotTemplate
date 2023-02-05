from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from loader import db


class IsAdmin(BoundFilter):
    async def check(self, message: types.Message):
        admins = await db.select_admin(tg_id=message.from_user.id)
        if admins:
            return True
