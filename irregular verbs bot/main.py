import selection
import data
import verbs
import buttons
import information
import telebot
from telebot import types
import random


# TOKEN
bot = telebot.TeleBot("5662650914:AAEG7-EHZ_2fuaaUa5Li2J8N_3kzDDw1lwE");


# START
@bot.message_handler(commands=['start'])
def start(message):
    msg = bot.send_message(message.from_user.id, text="Привет, {0.first_name}! Я бот для изучения английского языка! 👩‍💻".format(message.from_user), reply_markup=buttons.get_start())
    bot.register_next_step_handler(msg, t_functions)
    data.user[message.from_user.id] = []


# USER FUNCTIONS
@bot.message_handler(content_types=['text'])
def t_functions(message):
    if (message.text == "Привет 👋"):
        msg = bot.send_message(message.from_user.id, text="Привет! Давай учить неправильные глаголы 😊", reply_markup=buttons.start_learning())
        bot.register_next_step_handler(msg, t_irregular_verbs)
    elif (message.text == "Обратная связь 👩‍💻"):
        bot.send_message(message.from_user.id, "По всем вопросам обращайся к @kozyreva_k1 🙃")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю, напиши /start ✌️")


# GET USERS ANSWERS
def t_irregular_verbs(message):
    answer = message.text

    if (answer == "Давай 👀" or answer == "Ещё 🙂"):
        random_words, index = selection.get_random_word()
        random_translation = random.sample(selection.get_random_translation(index), k=4)

        msg = bot.send_message(message.from_user.id, text="Поставь слова в правильном порядке 🧐", reply_markup=buttons.new_verbs(random_words))
        bot.register_next_step_handler(msg, t_checking_1)

        data.user[message.from_user.id] = [verbs.first[index], 
                                           verbs.second[index], 
                                           verbs.third[index], 
                                           verbs.translate[index],
                                           random_words,
                                           random_translation]

        information.info(message.from_user, [verbs.first[index], verbs.second[index], verbs.third[index]], verbs.translate[index])

    elif (answer == "Стоп 🚫"):
        msg = bot.send_message(message.from_user.id, text="Эх, пока 😔", reply_markup=buttons.get_start_when_stop())
        bot.register_next_step_handler(msg, start)


# CHECK FIRST USER ANSWER
def t_checking_1(message):
    answer = message.text
    u_id = message.from_user.id

    if (answer == data.user[u_id][0]):
        msg = bot.send_message(message.from_user.id, "Молодец!\nТеперь 2 слово выберем 😌", reply_markup=buttons.get_verbs(u_id))
        bot.register_next_step_handler(msg, t_checking_2)
    else:
        msg = bot.send_message(message.from_user.id, "Неверно, слово «{0}» не подойдёт, попробуй ещё раз 👀".format(answer), reply_markup=buttons.get_verbs(u_id))
        bot.register_next_step_handler(msg, t_checking_1)


# CHECK SECOND USER ANSWER
def t_checking_2(message):
    answer = message.text
    u_id = message.from_user.id

    if (answer == data.user[u_id][1]):
        msg = bot.send_message(message.from_user.id, "Верно!\nВыберем 3 слово 😌", reply_markup=buttons.get_verbs(u_id))
        bot.register_next_step_handler(msg, t_checking_3)
    else:
        msg = bot.send_message(message.from_user.id, "Неверно, слово «{0}» не подойдёт, попробуй ещё раз 👀".format(answer), reply_markup=buttons.get_verbs(u_id))
        bot.register_next_step_handler(msg, t_checking_2)


# CHECK THIRD USER ANSWER
def t_checking_3(message):
    answer = message.text
    u_id = message.from_user.id

    if (answer == data.user[u_id][2]):
        msg = bot.send_message(message.from_user.id, "Правильно, молодец!\nА какой перевод у слова «{0}» ? 🙃".format(data.user[u_id][0]), reply_markup=buttons.get_translation(u_id))
        bot.register_next_step_handler(msg, translation)
    else:
        msg = bot.send_message(message.from_user.id, "Неверно, слово «{0}» не подойдёт, попробуй ещё раз 👀".format(answer), reply_markup=buttons.get_verbs(u_id))
        bot.register_next_step_handler(msg, t_checking_3)


# GET USER TRANSLATION
def translation(message):
    answer = message.text
    u_id = message.from_user.id

    if (answer == data.user[u_id][3]):
        msg = bot.send_message(message.from_user.id, text="Верно, учим дальше? 😊", reply_markup=buttons.get_stop_or_repeat())
        bot.register_next_step_handler(msg, t_irregular_verbs)
        data.user[message.from_user.id].clear()
    else:
        msg = bot.send_message(message.from_user.id, "Неверно, слово «{0}» так не переводится, попробуй ещё раз 👀".format(data.user[u_id][0]), reply_markup=buttons.get_translation(u_id))
        bot.register_next_step_handler(msg, translation)


bot.polling(none_stop=True)
