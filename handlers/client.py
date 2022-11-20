from aiogram import types, Dispatcher
from config import bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from ceybords.client_kb import start_markup
from database.bot_db import random_sql



async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_1")
    markup.add(button_call_1)
    question = 'Когда умер сталин ?'
    answer = [
        '1953',
        '1951',
        '1956',
        '1952'
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation='Learn new words',
        open_period=10,
        reply_markup=markup,

    )


# @dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await bot.send_message(message.chat.id, f'Hello {message.from_user.first_name}',
                           reply_markup = start_markup)



async def mem_handler(message: types.Message):
    photo = open("media/cover_6.jpg", 'rb')
    await bot.send_photo(message.chat.id, photo=photo)


async def dice_start(message: types.Message):
    await message.answer(f'This dice for BOT')
    bots = await bot.send_dice(message.chat.id, emoji='🎲')
    await message.answer(f'This dice for {message.from_user.full_name}')
    users = await bot.send_dice(message.chat.id, emoji='🎲')
    if bots.dice.value > users.dice.value:
        await message.answer(f'BOT won!'
                             f'\n{message.from_user.full_name}-{users.dice.value}'
                             f'\nBOT-{bots.dice.value}')
    elif bots.dice.value < users.dice.value:
        await message.answer(f'{message.from_user.full_name} won! '
                             f'\n{message.from_user.full_name}-{users.dice.value}'
                             f'\nBOT-{bots.dice.value}')

    else:
        await message.answer(f'draw (ничья)')


async def pin_message(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await message.answer(f'Your message {message.text} is not replied to message ')


async def get_random_mentor(message: types.Message):
    await random_sql(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(mem_handler, commands=['mem'])
    dp.register_message_handler(start_handler, commands=['start', 'help'])
    dp.register_message_handler(pin_message, commands=['pin'], commands_prefix='!')
    dp.register_message_handler(dice_start, commands=['dice'])
    dp.register_message_handler(get_random_mentor,commands=['get'])