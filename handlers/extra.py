import random
from aiogram import  Dispatcher, types
from config import bot, dp
from config import ADMINS




async def echo_1(message: types.Message):
    bad_words = ['мудак', 'лох', 'java','тварь', 'терпила']
    for word in bad_words:
        if word in message.text.lower():
            await  bot.send_message(
                message.chat.id,
                f'Не матерись @{message.from_user.username}'
                f'cам ты {word}'
            )
            await bot.delete_message(message.chat.id,message.message_id)
    if message.text.startswith('!pin'):
        if message.reply_to_message:
            await bot.pin_chat_message(message.chat.id,message.message_id)

    if message.text == 'game' and message.from_user.id in ADMINS:
        await bot.send_dice(message.chat.id, emoji= random.choice(['🎰','🎳','🎯','🎲','🏀','⚽']))

async def echo(message: types.Message):
    try:
        z = message.text
        x = int(z)
        c = x ** 2
        await bot.send_message(message.from_user.id, str(c))
    except:
        await bot.send_message(message.from_user.id, message.text)

def register_handlers_extra(dp:Dispatcher):
    dp.register_message_handler(echo_1)
    dp.register_message_handler(echo)


