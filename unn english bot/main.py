from tkinter.tix import Select
from deep_translator import GoogleTranslator
import random
import telebot
from telebot import types

# OPEN FILE
f = open("engwords.txt", "r")
words = f.read()
words_list = words.split("\n")

# GENERATE RANDOM WORDS
def get_random_word():
    random_words = random.choices(words_list, k=4)
    word = random.choice(random_words)
    return random_words, word


# TRANSLATE WORDS
def translation(words, word):
    r_answer = GoogleTranslator(source='en', target='ru').translate(word)
    w1 = GoogleTranslator(source='en', target='ru').translate(words[0]).lower()
    w2 = GoogleTranslator(source='en', target='ru').translate(words[1]).lower()
    w3 = GoogleTranslator(source='en', target='ru').translate(words[2]).lower()
    w4 = GoogleTranslator(source='en', target='ru').translate(words[3]).lower()
    translation_list = [w1, w2, w3, w4]
    return r_answer, translation_list


# TOKEN
bot = telebot.TeleBot("5431463396:AAGpCBdMOJ0ZoLhY2rZFjKyvnQOUrGrOBF4");

# START
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Поздороваться 👋")
    btn2 = types.KeyboardButton("Задать вопрос ❓")
    markup.add(btn1, btn2)
    msg = bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я бот для изучения английского языка!".format(message.from_user), reply_markup=markup)
    bot.register_next_step_handler(msg, t_functions)


# USER FUNCTIONS
@bot.message_handler(content_types=['text'])
def t_functions(message):
    if(message.text == "Поздороваться 👋"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        start = types.KeyboardButton("Давай 👀")
        markup.add(start)
        msg = bot.send_message(message.chat.id, text="Привет! Давай учить новые слова 😊", reply_markup=markup)
        bot.register_next_step_handler(msg, t_translation)
    elif(message.text == "Задать вопрос ❓"):
        bot.send_message(message.chat.id, "По всем вопросам обращайся к @kozyreva_k1")
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю, напиши /start ✌️")


# TRAINING
def t_translation(message):
    answer = message.text
    if (answer == "Давай 👀" or answer == "Ещё 🙂"):
        global random_words, word
        global r_answer, translation_list

        random_words, word = get_random_word()
        r_answer, translation_list = translation(random_words, word)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        trn1 = types.KeyboardButton(translation_list[0])
        trn2 = types.KeyboardButton(translation_list[1])
        trn3 = types.KeyboardButton(translation_list[2])
        trn4 = types.KeyboardButton(translation_list[3])
        markup.add(trn1, trn2, trn3, trn4)
        msg = bot.send_message(message.chat.id, text="Выбери перевод слова << {0} >>".format(word), reply_markup=markup)
        bot.register_next_step_handler(msg, t_checking)
    elif (answer == "Стоп 🚫"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Поздороваться 👋")
        btn2 = types.KeyboardButton("Задать вопрос ❓")
        markup.add(btn1, btn2)
        msg = bot.send_message(message.chat.id, text="Эх, пока 😔", reply_markup=markup)
        bot.register_next_step_handler(msg, t_functions)


# CHECK USER ANSWER
def t_checking(message):
    if (message.text == r_answer):
        bot.send_message(message.chat.id, "Верно, молодец!")

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        repeat = types.KeyboardButton("Ещё 🙂")
        stop = types.KeyboardButton("Стоп 🚫")
        markup.add(repeat, stop)

        msg = bot.send_message(message.chat.id, text="Ещё? 🙃", reply_markup=markup)
        bot.register_next_step_handler(msg, t_translation)
    elif (message.text != r_answer):
        bot.send_message(message.chat.id, "Неверно, слово << {0} >> переводится как << {1} >>".format(word, r_answer))

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        repeat = types.KeyboardButton("Ещё 🙂")
        stop = types.KeyboardButton("Стоп 🚫")
        markup.add(repeat, stop)

        msg = bot.send_message(message.chat.id, text="Ещё? 🙃", reply_markup=markup)
        bot.register_next_step_handler(msg, t_translation)


bot.polling(none_stop=True)
