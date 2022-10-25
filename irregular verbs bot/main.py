import selection
import data
import verbs
import telebot
from telebot import types


# TOKEN
bot = telebot.TeleBot("5662650914:AAEG7-EHZ_2fuaaUa5Li2J8N_3kzDDw1...");

# START
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Привет 👋")
    btn2 = types.KeyboardButton("Обратная связь 👩‍💻")
    markup.add(btn1, btn2)
    msg = bot.send_message(message.from_user.id, text="Привет, {0.first_name}! Я бот для изучения английского языка! 👩‍💻".format(message.from_user), reply_markup=markup)
    bot.register_next_step_handler(msg, t_functions)
    data.user[message.from_user.id] = []


# USER FUNCTIONS
@bot.message_handler(content_types=['text'])
def t_functions(message):
    if (message.text == "Привет 👋"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        start = types.KeyboardButton("Давай 👀")
        markup.add(start)
        msg = bot.send_message(message.from_user.id, text="Привет! Давай учить неправильные глаголы 😊", reply_markup=markup)
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
        random_translation = selection.get_random_translation(index)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        f_word = types.KeyboardButton(random_words[0])
        s_word = types.KeyboardButton(random_words[1])
        t_word = types.KeyboardButton(random_words[2])
        markup.add(f_word, s_word, t_word)

        msg = bot.send_message(message.from_user.id, text="Поставь слова в правильном порядке 🧐", reply_markup=markup)
        bot.register_next_step_handler(msg, t_checking_1)
        data.user[message.from_user.id] = [verbs.first[index], 
                                        verbs.second[index], 
                                        verbs.third[index], 
                                        verbs.translate[index],
                                        random_words,
                                        random_translation]
    elif (answer == "Стоп 🚫"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("/start")
        markup.add(btn1)
        msg = bot.send_message(message.from_user.id, text="Эх, пока 😔", reply_markup=markup)
        bot.register_next_step_handler(msg, start)


# CHECK FIRST USER ANSWER
def t_checking_1(message):
    answer = message.text
    u_id = message.from_user.id

    if (answer == data.user[u_id][0]):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        f_word = types.KeyboardButton(data.user[u_id][-2][0])
        s_word = types.KeyboardButton(data.user[u_id][-2][1])
        t_word = types.KeyboardButton(data.user[u_id][-2][2])
        markup.add(f_word, s_word, t_word)
        msg = bot.send_message(message.from_user.id, "Молодец!\nТеперь 2 слово выберем 😌", reply_markup=markup)
        bot.register_next_step_handler(msg, t_checking_2)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        f_word = types.KeyboardButton(data.user[u_id][-2][0])
        s_word = types.KeyboardButton(data.user[u_id][-2][1])
        t_word = types.KeyboardButton(data.user[u_id][-2][2])
        markup.add(f_word, s_word, t_word)
        msg = bot.send_message(message.from_user.id, "Неверно, слово «{0}» не подойдёт, попробуй ещё раз 👀".format(answer), reply_markup=markup)
        bot.register_next_step_handler(msg, t_checking_1)


# CHECK SECOND USER ANSWER
def t_checking_2(message):
    answer = message.text
    u_id = message.from_user.id

    if (answer == data.user[u_id][1]):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        f_word = types.KeyboardButton(data.user[u_id][-2][0])
        s_word = types.KeyboardButton(data.user[u_id][-2][1])
        t_word = types.KeyboardButton(data.user[u_id][-2][2])
        markup.add(f_word, s_word, t_word)
        msg = bot.send_message(message.from_user.id, "Верно!\nВыберем 3 слово 😌", reply_markup=markup)
        bot.register_next_step_handler(msg, t_checking_3)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        f_word = types.KeyboardButton(data.user[u_id][-2][0])
        s_word = types.KeyboardButton(data.user[u_id][-2][1])
        t_word = types.KeyboardButton(data.user[u_id][-2][2])
        markup.add(f_word, s_word, t_word)
        msg = bot.send_message(message.from_user.id, "Неверно, слово «{0}» не подойдёт, попробуй ещё раз 👀".format(answer), reply_markup=markup)
        bot.register_next_step_handler(msg, t_checking_2)


# CHECK THIRD USER ANSWER
def t_checking_3(message):
    answer = message.text
    u_id = message.from_user.id

    if (answer == data.user[u_id][2]):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        trns_1 = types.KeyboardButton(data.user[u_id][-1][0])
        trns_2 = types.KeyboardButton(data.user[u_id][-1][1])
        trns_3 = types.KeyboardButton(data.user[u_id][-1][2])
        trns_4 = types.KeyboardButton(data.user[u_id][-1][3])
        markup.add(trns_1, trns_2, trns_3, trns_4)
        msg = bot.send_message(message.from_user.id, "Правильно, молодец!\nА какой перевод у слова «{0}» ? 🙃".format(data.user[u_id][0]), reply_markup=markup)
        bot.register_next_step_handler(msg, translation)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        f_word = types.KeyboardButton(data.user[u_id][-2][0])
        s_word = types.KeyboardButton(data.user[u_id][-2][1])
        t_word = types.KeyboardButton(data.user[u_id][-2][2])
        markup.add(f_word, s_word, t_word)
        msg = bot.send_message(message.from_user.id, "Неверно, слово «{0}» не подойдёт, попробуй ещё раз 👀".format(answer), reply_markup=markup)
        bot.register_next_step_handler(msg, t_checking_3)


# GET USER TRANSLATION
def translation(message):
    answer = message.text
    u_id = message.from_user.id

    if (answer == data.user[u_id][3]):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        repeat = types.KeyboardButton("Ещё 🙂")
        stop = types.KeyboardButton("Стоп 🚫")
        markup.add(repeat, stop)
        msg = bot.send_message(message.from_user.id, text="Верно, учим дальше? 😊", reply_markup=markup)
        bot.register_next_step_handler(msg, t_irregular_verbs)
        data.user[message.from_user.id].clear()
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        trns_1 = types.KeyboardButton(data.user[u_id][-1][0])
        trns_2 = types.KeyboardButton(data.user[u_id][-1][1])
        trns_3 = types.KeyboardButton(data.user[u_id][-1][2])
        trns_4 = types.KeyboardButton(data.user[u_id][-1][3])
        markup.add(trns_1, trns_2, trns_3, trns_4)
        msg = bot.send_message(message.from_user.id, "Неверно, слово «{0}» так не переводится, попробуй ещё раз 👀".format(data.user[u_id][0]), reply_markup=markup)
        bot.register_next_step_handler(msg, translation)


bot.polling(none_stop=True)
