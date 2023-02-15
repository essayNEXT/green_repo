# from aiogram import types, Dispatcher
# from aiogram.dispatcher import FSMContext
# from aiogram.utils.markdown import hcode
# from bot import Bot, Dispatcher
import time
from aiogram import types
from aiogram.types import CallbackQuery
from tgbot.keyboards.inline import main_keyboard
from bot import bot, dp
from tgbot.config import admin_id
from datetime import datetime


async def send_to_admin(dp):
    " Функція відправки повідомлення адміну"
    await bot.send_message(chat_id=admin_id, text="Бот активований")
    await bot.send_message(chat_id=admin_id, text="Натисніть   /start")

async def on_shutdown(dp):
    await bot.send_message(chat_id=admin_id, text="Бот деактивовано")
    await bot.close()

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    user_full_name = message.from_user.full_name
    timestamp_now = datetime.now()
    await bot.send_message(user_id, text="Вітаю, я телеграм бот")
    time.sleep(2)
    await bot.send_message(user_id,
                           text=f"Данні відправника повідомлення:\n"
                                f"user_id: {user_id}\n"
                                f"first_name: {first_name}\n"
                                f"last_name: {last_name}\n"
                                f"user_full_name: {user_full_name}\n"
                                f"time: {timestamp_now}")


@dp.message_handler()
async def any_massage_handler(message: types.Message):
    user_id = message.from_user.id
    data = datetime.now()
    await bot.send_message(user_id, text=f"Прошу відмітити свою присутність на уроці {data}",
                           reply_markup=main_keyboard)

