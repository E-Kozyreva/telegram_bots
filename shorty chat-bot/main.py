import telebot
from telebot import types
import buttons
import books


# TOKEN
bot = telebot.TeleBot("5634218236:AAE5ECZb4LXJE75AGEpOuSLT9GRtwrccEE8");


# START
@bot.message_handler(commands=['start'])  
def t_start_command(message):  
    bot.send_message(message.chat.id,  "Привет, я чат-бот!")


# GET BOOK
@bot.message_handler(commands=["books"])
def t_get_book(message):
    msg = bot.send_message(message.chat.id, text="Выбери файл, который хочешь скачать 🙃", reply_markup=buttons.get_book())
    bot.register_next_step_handler(msg, t_send_book)


def t_send_book(message):
    answer = message.text
    if answer in books.book:
        bot.send_document(message.chat.id, document=books.book[answer], reply_markup=types.ReplyKeyboardRemove())
    else:
        msg = bot.send_message(message.chat.id, text="Такого файла нет, попробуй ещё раз 😔", reply_markup=buttons.get_book())
        bot.register_next_step_handler(msg, t_send_book)


bot.polling(none_stop=True)
