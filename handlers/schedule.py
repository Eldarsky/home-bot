import  aioschedule
from aiogram import types, Dispatcher
from config import bot
import asyncio

async def  get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await message.answer('Без проблем')

async def to_sleep():
    await bot.send_message(chat_id=chat_id, text="Элдар сегодня у вас учеба в GeekTech")

async def wake_up():
    photo = open('media/motiviruyhie_cytaty.jpg', 'rb')
    await bot.send_photo(chat_id=chat_id, photo=photo,
                         caption="Иди к цели в GeekTech")

async def scheduler():
    aioschedule.every().friday.at('17:00').do(to_sleep)
    aioschedule.every().day.at('17:05').do(wake_up)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)







def register_handlers_schedule(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: 'напомни' in word.text)
