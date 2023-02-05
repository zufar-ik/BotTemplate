from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    await message.answer(f'🤔 Что делает этот бот!?:\n\n'
                         f'...')
    await message.answer(f'Команды: \n'
                         f'/start - Запуск бота\n'
                         f'/help - Помощь')
