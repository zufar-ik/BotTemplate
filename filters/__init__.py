from aiogram import Dispatcher

from filters.admin_filter import IsAdmin
from loader import dp

def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsAdmin)