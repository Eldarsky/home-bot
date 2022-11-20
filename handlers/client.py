from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp
from database.bot_db import sql_command_random


# @dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f"Здравствуйте!! {message.from_user.first_name}")


async def info_handler(message: types.Message):
    await message.reply('Этот просто Инфо тут ничего нету')


# @dp.message_handler(commands=['quiz'])
async def quiz(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('NEXT', callback_data='button_call_1')
    markup.add(button_call_1)
    question = "в каком году распался ссср"
    answers = [
        "1995",
        '1993',
        '1992',
        '1991',
        '1999',
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Правильный ответ '1991",
        reply_markup=markup

    )

async  def get_random_user(message: types.Message):
    await sql_command_random(message)
async def mem(call: types.CallbackQuery):



    photo = open('media/cover_6.jpg', 'rb')
    await bot.send_photo(call.from_user.id,photo=photo)



def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(quiz, commands=['quiz'])
    dp.register_message_handler(info_handler, commands=['info'])
    dp.register_message_handler(mem,commands=['mem'])
    dp.register_message_handler(get_random_user,commands=['get'])
