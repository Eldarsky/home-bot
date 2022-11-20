from aiogram import  Dispatcher, types
from aiogram import Dispatcher, types
from config import bot, ADMINS
from database.bot_db import sql_command_all, sql_command_delete, sql_command_get_all_ids
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def ban(message: types.Message):
    if message.chat.type == "group":
        if message.from_user.id not in ADMINS:
            await message.answer("Ты не мой босс!")
        elif not message.reply_to_message:
            await message.answer("Команда должна быть ответом на сообщение!")
        else:
            await bot.kick_chat_member(message.chat.id,
                                       message.reply_to_message.from_user.id)
            await message.answer(f'{message.from_user.first_name} братан кикнул '
                                 f'{message.reply_to_message.from_user.full_name}')
    else:
        await message.answer("Пиши в группе!")

async def delete_data(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.answer("Ты не мой босс!")
    else:
        users = await sql_command_all()
        for user in users:
            await bot.send_photo(message.chat.id, user[1],
                                 caption=f"{user[2]} {user[3]} {user[4]}",
                                 reply_markup= InlineKeyboardMarkup().add(
                                     InlineKeyboardButton(f'delete {user [1]}',
                                                          callback_data=f'delete {user[0]}')
                                 )

                                 )


async def rassylka(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.answer("Ты не мой босс!")
    else:
        user_ids = await sql_command_get_all_ids()
        for user_id in user_ids:
            await bot.send_message(user_id[0], message.text.replace('/R ', ''))

async def complete_delete(call: types.CallbackQuery):
    await sql_command_delete(call.data.replace('delete ', ''))
    await call.answer(text="Поки поки!", show_alert=True)
    await bot.delete_message(call.from_user.id, call.message.message_id)



def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix='!/')
    dp.register_message_handler(delete_data, commands=['del'])
    dp.register_message_handler(rassylka, commands=['R'])
    dp.register_callback_query_handler(complete_delete,
                                       lambda call: call.data and call.data.startswith("delete "))