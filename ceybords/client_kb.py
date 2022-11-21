from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=2,

).add(
    KeyboardButton('/quiz'),
    KeyboardButton('/mem'),
    KeyboardButton('/dice'),
    KeyboardButton('/help'),
    KeyboardButton('/reg'),
    KeyboardButton('/get'),
    KeyboardButton('/del'),

)

submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(
    KeyboardButton("ДА"),
    KeyboardButton("НЕТ"),

)

cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(
    KeyboardButton("CANCEL")
)
part_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width = 3,
).add(
    KeyboardButton("JAVA"),
    KeyboardButton("PHP"),
    KeyboardButton("JAVASCRIPTS"),
    KeyboardButton("C"),
    KeyboardButton('C++'),
    KeyboardButton('SQL'),
    KeyboardButton('PYTHON')
)