from aiogram import  Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp
#@dp.callback_query_handler(text="button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data='button_call_2')
    markup.add(button_call_2)


    question = "В каком году умер Сталин ?"
    answers = [
        "1953 г.",
        "1952 г.",
        "1955 г.",
        "1954 г.",
        "1956 г.",
        "1957 г.",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Правильный ответ 1953 г.",
        reply_markup=markup
    )
async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("NEXT", callback_data='button_call_3')
    markup.add(button_call_3)


    question = "В каком году вышел телефон ?"
    answers = [
        "1875 г.",
        "1874 г.",
        "1876 г.",
        "1878 г.",
        "1877 г.",
        "1872 г.",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Правильный ответ 1876 г.",
        reply_markup=markup
    )
#@dp.callback_query_handler(lambda call: call.data == "button_call_2")

def register_handlers_collback(dp:Dispatcher):
    dp.register_callback_query_handler(quiz_2,text="button_call_1")
    dp.register_callback_query_handler(quiz_3, text="button_call_2")