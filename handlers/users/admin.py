import asyncio
import os
import sqlite3
import aiogram
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from filters import IsAdmin
from keyboards.default.menu import cancel
from keyboards.inline.menu_adm import yes_no
from loader import dp, db, bot
from states.state import Forward


@dp.message_handler(IsAdmin(), text="/reklama", state='*')
async def send_ad_to_all(message: types.Message):
    await message.answer('Начнем строить рекламу!')
    await message.answer('Хотите добавить кнопки?', reply_markup=yes_no)
    await Forward.one.set()


@dp.callback_query_handler(state=Forward.one)
async def inline(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'yes':
        await call.message.answer('Введите название кнопки!', reply_markup=ReplyKeyboardRemove())
        await Forward.two.set()
    else:
        await call.message.answer("Перешлите сообщение с канала/пользователя для пересылки!\n"
                                  "Важно чтобы бот был администратором канала!", reply_markup=cancel)
        await Forward.four.set()


@dp.message_handler(state=Forward.two)
async def yes_no_in(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data(
        {'text': text}
    )
    await message.answer('Введите ссылку для кнопки!')
    await Forward.three.set()


@dp.message_handler(state=Forward.three)
async def yes_in(message: types.Message, state: FSMContext):
    url = message.text
    await state.update_data(
        {'url': url}
    )
    await message.answer("Перешлите сообщение с канала/пользователя для пересылки!\n"
                         "Важно чтобы бот был администратором канала!", reply_markup=cancel)
    await Forward.four.set()


@dp.message_handler(content_types=types.ContentType.ANY, state=Forward.four)
async def answer_fullname(message: types.Message, state: FSMContext):
    data = await state.get_data()
    text = data.get('text')
    url = data.get('url')
    reply = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=f'{text}', url=f'{url}')]
        ]
    )
    if message.text != "Отменить":
        try:
            cnt = 0
            users = await db.select_all_users()
            for user in users:
                try:
                    try:
                        try:
                            try:
                                await bot.copy_message(chat_id=user['tg_id'],
                                                       from_chat_id=message.forward_from_chat.id,
                                                       message_id=message.forward_from_message_id, reply_markup=reply)
                                cnt += 1
                                await asyncio.sleep(0.07)
                            except aiogram.utils.exceptions.BadRequest:
                                await bot.copy_message(chat_id=user['tg_id'],
                                                       from_chat_id=message.forward_from_chat.id,
                                                       message_id=message.forward_from_message_id)
                                cnt += 1
                                await asyncio.sleep(0.07)
                        except aiogram.utils.exceptions.ChatNotFound:
                            pass
                    except aiogram.utils.exceptions.MessageToForwardNotFound:
                        await message.answer('1.Бот не является админом этого канала\n'
                                             '2.Сообщение не найдено!')
                        await state.finish()
                        break
                except aiogram.utils.exceptions.BotBlocked:
                    pass
            await message.answer("Отправка пользователя прошла успешно!\n"
                                 f"Отправил {cnt} пользователю")
            await state.finish()
        except AttributeError:
            await message.answer('Перешлите мне сообщение!')

    else:
        await message.answer("Отменено!")
        await state.finish()
