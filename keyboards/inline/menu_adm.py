from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
yes_no = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Да', callback_data='yes')],
        [InlineKeyboardButton(text='Нет', callback_data='no')]
    ]
)