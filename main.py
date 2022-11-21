from aiogram.utils import executor
from config import dp
import logging
from handlers import client, collback, extra, admin, fsm_anketa
from database.bot_db import sql_create
async def on_startup(_):
    sql_create()

client.register_handlers_client(dp)
collback.register_handlers_collback(dp)
admin.register_handlers_admin(dp)
fsm_anketa.register_handlers_fsm_anketa(dp)
extra.register_handlers_extra(dp)
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp,skip_updates= True, on_startup=on_startup)









