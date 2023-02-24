import time
from aiogram import types
from aiogram.types import CallbackQuery
from tg_bot.keyboards.inline import main_keyboard, categories_keyboard
from bot import bot, dp
from tg_bot.config import admin_id
from datetime import datetime
from typing import Union

async def send_to_admin(dp):
    " Функція відправки повідомлення адміну"
    await bot.send_message(chat_id=admin_id, text="Бот активований")
    await bot.send_message(chat_id=admin_id, text="Натисніть   /start")


async def on_shutdown(dp):
    await bot.send_message(chat_id=admin_id, text="Бот деактивовано")
    await bot.session.close()


@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    user_full_name = message.from_user.full_name
    timestamp_now = datetime.now()
    await bot.send_message(user_id, text=f"Вітаю, {user_full_name}")
    time.sleep(2)
    # await bot.send_message(user_id,
    #                        text=f"Данні відправника повідомлення:\n"
    #                             f"user_id: {user_id}\n"
    #                             f"first_name: {first_name}\n"
    #                             f"last_name: {last_name}\n"
    #                             f"user_full_name: {user_full_name}\n"
    #                             f"time: {timestamp_now}")
    await bot.send_message(user_id, text="Основне меню: ",
                           reply_markup=categories_keyboard)


@dp.callback_query_handler(text="start")
async def start_handler(call: CallbackQuery):
    await call.message.answer(text=f"Вітаю {call.from_user.full_name}. Я Study_Bot і допоможу тобі у навчанні. Тисни на"
                                   f" 'Що вміє бот' і дізнаєшся, що вмію")


@dp.callback_query_handler(text="help")
async def help_handler(call: CallbackQuery):
    await call.message.answer(
        text="Цей бот вміє:\n"
             "1. Допомагати студентам;\n"
             "2. Допомагати викладачам;\n"
             "3. Відмічати присутність студентів на уроці;\n"
             "4. Відправка посинань з домашнім завданням;\n"
             "5. Проведення тестування для студентів:\n"
             "6. _________")


@dp.callback_query_handler(text="register")
async def register_handler(call: CallbackQuery):
    await call.message.answer(text="Прописати дії для команди 'Реєстрація студента'")


@dp.callback_query_handler(text="about_me")
async def about_me_handler(call: CallbackQuery):
    user_id = call.from_user.id
    full_name = call.from_user.full_name
    await call.message.answer(text=f"Інформація про студента - {full_name}:\n"
                                   f"ваша група: __\n"
                                   f"рейтинг: __\n"
                                   f"середня оцінка: __\n"
                                   f"відсоток виконання домашнього завдання: __")


@dp.callback_query_handler(text="mark_in_class")
async def mark_in_class_handler(call: CallbackQuery):
    data = datetime.now()
    await call.message.answer(text=f"Прошу відмітити свою присутність на уроці {data.date()}",
                              reply_markup=main_keyboard)

@dp.callback_query_handler(text="present")
async def present_handler(call: CallbackQuery):
    # print("present_handler")
    # print(call)
    if call.data == "present":
        await call.message.answer(text="Ваша присутність занесена в базу")
    else:
        await call.message.answer(text="Надіюсь, побачимось наступного уроку")








# from aiogram import types, Dispatcher
# from aiogram.dispatcher import FSMContext
# from aiogram.utils.markdown import hcode
#
#
# async def bot_echo(message: types.Message):
#     text = [
#         "Эхо без состояния.",
#         "Сообщение:",
#         message.text
#     ]
#
#     await message.answer('\n'.join(text))
#
#
# async def bot_echo_all(message: types.Message, state: FSMContext):
#     state_name = await state.get_state()
#     text = [
#         f'Эхо в состоянии {hcode(state_name)}',
#         'Содержание сообщения:',
#         hcode(message.text)
#     ]
#     await message.answer('\n'.join(text))
#
#
# def register_echo(dp: Dispatcher):
#     dp.register_message_handler(bot_echo)
#     dp.register_message_handler(bot_echo_all, state="*", content_types=types.ContentTypes.ANY)
