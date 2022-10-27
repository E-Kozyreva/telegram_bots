import data
from telebot import types


def get_start():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Привет 👋")
    btn2 = types.KeyboardButton("Обратная связь 👩‍💻")
    return markup.add(btn1, btn2)


def start_learning():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start = types.KeyboardButton("Давай 👀")
    return markup.add(start)


def get_stop_or_repeat():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    repeat = types.KeyboardButton("Ещё 🙂")
    stop = types.KeyboardButton("Стоп 🚫")
    return markup.add(repeat, stop)


def new_verbs(random_words):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    f_word = types.KeyboardButton(random_words[0])
    s_word = types.KeyboardButton(random_words[1])
    t_word = types.KeyboardButton(random_words[2])
    return markup.add(f_word, s_word, t_word)


def get_verbs(user_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    f_word = types.KeyboardButton(data.user[user_id][-2][0])
    s_word = types.KeyboardButton(data.user[user_id][-2][1])
    t_word = types.KeyboardButton(data.user[user_id][-2][2])
    return markup.add(f_word, s_word, t_word)


def get_translation(user_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    trns_1 = types.KeyboardButton(data.user[user_id][-1][0])
    trns_2 = types.KeyboardButton(data.user[user_id][-1][1])
    trns_3 = types.KeyboardButton(data.user[user_id][-1][2])
    trns_4 = types.KeyboardButton(data.user[user_id][-1][3])
    return markup.add(trns_1, trns_2, trns_3, trns_4)


def get_start_when_stop():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/start")
    return markup.add(btn1)
