from aiogram import types, Dispatcher
from aiogram.dispatcher import  FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State,StatesGroup
from config import bot
from ceybords.client_kb import submit_markup, cancel_markup, part_markup
from config import ADMINS
from database.bot_db import sql_command_insert

class FSMadmin(StatesGroup):
    name = State()
    directions = State()
    age = State()
    krupa = State()
    submit = State()
async  def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id in ADMINS:
            await FSMadmin.name.set()
            await message.answer("Здравствуйте как вас зовут?",
                                 reply_markup=cancel_markup)
    else:
        await message.answer("Пиши в личку!")


async def load_name(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMadmin.next()
    await message.answer('Какое направления?', reply_markup=submit_markup)

async def load_directions(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['directions'] = message.text
    await FSMadmin.next()
    await message.answer("Сколько вам лет ??",)

async def load_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text
    await FSMadmin.next()
    await message.answer("Ваша Язык программирования??",reply_markup=part_markup)

async def load_krupa(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['krupa'] = message.text
        await message.answer(f"\nName: {data['name']}"
                             f"\ndirections: {data['directions']}"
                             f"\nage: {data['age']}"
                             f"\nkrupa: {data['krupa']}")
        await FSMadmin.next()
        await message.answer('Все данные правильны?', reply_markup=submit_markup)

async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        await sql_command_insert(state)
        await state.finish()
        await message.answer("Все свободен!")
    elif message.text.lower() == "нет":
        await state.finish()
        await message.answer("Отмена")
    else:
        await message.answer("Нипонял!?")

async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("Отмена")


def register_handlers_fsm_anketa(dp:Dispatcher):
    dp.register_message_handler(cancel_reg, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_reg, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_name,state=FSMadmin.name)
    dp.register_message_handler(load_directions, state=FSMadmin.directions)
    dp.register_message_handler(load_age, state=FSMadmin.age)
    dp.register_message_handler(load_krupa, state=FSMadmin.krupa)
    dp.register_message_handler(submit, state=FSMadmin.submit)
