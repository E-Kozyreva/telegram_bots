from telebot import types

def commands():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("/start")
    btn2 = types.KeyboardButton("/commands")
    btn3 = types.KeyboardButton("/books")
    btn4 = types.KeyboardButton("/tasks")
    btn5 = types.KeyboardButton("/homework")
    btn6 = types.KeyboardButton("/info")
    return markup.add(btn1, btn2, btn3, btn4, btn5, btn6)


def get_book():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton("Идивидуальное чтение")
    btn2 = types.KeyboardButton("English for mathematics")
    btn3 = types.KeyboardButton("Test your English")
    btn4 = types.KeyboardButton("Перевод англоязычных текстов")
    btn5 = types.KeyboardButton("Remedial English")
    return markup.add(btn1, btn2, btn3, btn4, btn5)

