from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo, MenuButtonWebApp

cancel = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Отмена!')]
    ],
    resize_keyboard=True
)
