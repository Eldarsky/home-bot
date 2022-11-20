from aiogram.utils import executor
import logging
from config import dp
from handlers import admin, client, collback, extra, fsm_anketa
from database.bot_db import create_sql


async def on_startup(_):
    create_sql()


client.register_handlers_client(dp)
collback.register_callback_handlers(dp)
fsm_anketa.register_handlers_fsm_mentor(dp)
admin.register_admin_handler(dp)
extra.register_extra_handler(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)










