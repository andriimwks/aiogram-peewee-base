from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.i18n import I18nMiddleware
from app.config import TELEGRAM_TOKEN, LOCALES_DIR, I18N_DOMAIN
from app.models import *

bot = Bot(TELEGRAM_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())
i18n = I18nMiddleware(I18N_DOMAIN, LOCALES_DIR)
_ = i18n.gettext

def setup() -> None:
    dp.middleware.setup(i18n)
    import app.handlers
