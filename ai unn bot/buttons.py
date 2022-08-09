from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

say_hi = KeyboardButton('Привет 👋')
hi = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(say_hi)

traning1 = KeyboardButton('Английский -> Русский')
traning2 = KeyboardButton('Русский -> Английский')
traning = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(traning1).add(traning2)
