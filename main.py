from aiogram.utils import executor
from config import dp
import logging
from handlers import client, collback, extra
client.register_handlers_client(dp)
collback.register_handlers_collback(dp)
extra.register_handlers_extra(dp)
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp,skip_updates= True)









