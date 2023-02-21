from aiogram import executor
from app import misc
from app.models import *

async def on_shutdown(_) -> None:
    db.close()

def run_bot() -> None:
    misc.setup()
    db.setup(User)

    executor.start_polling(
        dispatcher=misc.dp,
        skip_updates=True,
        on_shutdown=on_shutdown
    )
