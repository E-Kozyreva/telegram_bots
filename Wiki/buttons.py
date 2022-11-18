import telebot


def get_hi():
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    return keyboard.row("Привет 👋🏻")


def get_article():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
    return keyboard.row("Найти статью в Wikipedia 🔍", "Случайная статья 🤔")


def get_new_function():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
    return keyboard.row("Да ✅", "Нет ❌")
