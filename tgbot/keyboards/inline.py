from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

present_button = InlineKeyboardButton(text="ПРИСУТНІЙ", callback_data="present")
absent_button = InlineKeyboardButton(text="ВІДСУТНІЙ", callback_data="absent")

main_keyboard = InlineKeyboardMarkup(row_width=1).add(present_button, absent_button)


