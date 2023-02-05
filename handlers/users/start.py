import asyncpg
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from filters import IsAdmin
from loader import db, bot
from loader import dp


@dp.message_handler(IsAdmin(), CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer('Добро пожаловать!')


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    try:
        admins = await db.select_all_admin()
        await db.add_user(tg_id=message.from_user.id, username=message.from_user.username,
                          first_name=message.from_user.first_name)
        count = await db.count_users()
        for admin in admins:
            try:
                await bot.send_message(chat_id=admin['tg_id'],
                                       text=f'В базе новый <a href="https://t.me/{message.from_user.username}">пользователь</a>!\n'
                                            f'В базе {count} пользоателей',disable_web_page_preview=True)
            except:
                pass
        await message.answer(f'Добро пожаловать {message.from_user.first_name}')
    except asyncpg.exceptions.UniqueViolationError:
        await message.answer(f'С возращением {message.from_user.first_name}')
