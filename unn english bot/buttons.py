import data
from telebot import types


def get_first_message():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Поздороваться 👋")
    btn2 = types.KeyboardButton("Обратная связь 👩‍💻")
    return markup.add(btn1, btn2)


def hello():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start = types.KeyboardButton("Давай 👀")
    return markup.add(start)


def user_data(u_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    trn1 = types.KeyboardButton(data.user_answer[u_id][0][0])
    trn2 = types.KeyboardButton(data.user_answer[u_id][0][1])
    trn3 = types.KeyboardButton(data.user_answer[u_id][0][2])
    trn4 = types.KeyboardButton(data.user_answer[u_id][0][3])
    return markup.add(trn1, trn2, trn3, trn4)


def repeat():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    repeat = types.KeyboardButton("Ещё 🙂")
    stop = types.KeyboardButton("Стоп 🚫")
    return markup.add(repeat, stop)


def stop():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("/start")
    return markup.add(btn)
