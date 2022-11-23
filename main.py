import asyncio
from aiogram.utils import executor
from config import dp
import logging
from handlers import client, collback, extra, admin, fsm_anketa, schedule
from database.bot_db import sql_create
async def on_startup(_):
    asyncio.create_task(schedule.scheduler())
    sql_create()

client.register_handlers_client(dp)
collback.register_callback_handlers(dp)
fsm_anketa.register_handlers_fsm_anketa(dp)
schedule.register_handlers_schedule(dp)
admin.register_admin_handler(dp)

extra.register_extra_handler(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp,skip_updates= True, on_startup=on_startup)









