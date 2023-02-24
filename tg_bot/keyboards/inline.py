from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

present_button = InlineKeyboardButton(text="ПРИСУТНІЙ", callback_data="present")
absent_button = InlineKeyboardButton(text="ВІДСУТНІЙ", callback_data="absent")
main_keyboard = InlineKeyboardMarkup(row_width=1).add(present_button, absent_button)


start = InlineKeyboardButton(text="Старт", callback_data="start")
help_me = InlineKeyboardButton(text="Що вміє бот", callback_data="help")
register = InlineKeyboardButton(text="Реєстрація студента", callback_data="register")
about_me = InlineKeyboardButton(text="Про мене", callback_data="about_me")
mark_in_class = InlineKeyboardButton(text="Відмітитись на уроці", callback_data="mark_in_class")

categories_keyboard = InlineKeyboardMarkup(row_width=2).add(start, help_me, register, about_me, mark_in_class)
