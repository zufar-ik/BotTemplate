from aiogram import Bot, Dispatcher, types
from utils.db_api.db_commands import Database
from data import config
from aiogram.contrib.fsm_storage.redis import RedisStorage2
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

storage = RedisStorage2()
dp = Dispatcher(bot, storage=storage)
db = Database()
