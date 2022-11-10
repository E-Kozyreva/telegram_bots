import telebot
from telebot import types
import books
import buttons


# TOKEN
bot = telebot.TeleBot("5634218236:AAE5ECZb4LXJE75AGEpOuSLT9GRtwrccEE8");
url = "https://api.telegram.org/bot"


# START
@bot.message_handler(commands=['start'])  
def start_command(message):  
    bot.send_message(message.chat.id,  "Привет, я чат-бот!")


# GET BOOKS
@bot.message_handler(commands=["get_book"])
def t_get_book(message):
    msg = bot.send_message(message.chat.id, text="Выбери файл :)", reply_markup=buttons.get_book())
    bot.register_next_step_handler(msg, t_send_book)


def t_send_book(message):
    answer = message.text
    if answer in books.book:
        pdf = open(f'files/{answer}.pdf', 'rb')
        bot.send_document(message.chat.id, pdf)
        pdf.close()
    else:
        msg = bot.send_message(message.chat.id, text="Такого файла нет, попробуй ещё раз", reply_markup=buttons.get_book())
        bot.register_next_step_handler(msg, t_send_book)


bot.polling(none_stop=True)
