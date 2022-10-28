import telebot
import data
import buttons
import translate
from telebot import types


# TOKEN
bot = telebot.TeleBot("5431463396:AAGpCBdMOJ0ZoLhY2rZFjKyvnQOUrGrO...");


# START
@bot.message_handler(commands=['start'])
def start(message):
    msg = bot.send_message(message.from_user.id, text="Привет, {0.first_name}! Я бот для изучения английского языка! 👩‍💻".format(message.from_user), reply_markup=buttons.get_first_message())
    bot.register_next_step_handler(msg, t_functions)


# USER FUNCTIONS
@bot.message_handler(content_types=['text'])
def t_functions(message):
    if(message.text == "Поздороваться 👋"):
        msg = bot.send_message(message.from_user.id, text="Привет! Давай учить новые слова 😊", reply_markup=buttons.hello())
        bot.register_next_step_handler(msg, t_translation)
    elif(message.text == "Обратная связь 👩‍💻"):
        bot.send_message(message.from_user.id, "По всем вопросам обращайся к @kozyreva_k1 🙃")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю, напиши /start ✌️")


# TRAINING
def t_translation(message):
    answer = message.text
    if (answer == "Давай 👀" or answer == "Ещё 🙂"):
        global random_words, word
        global r_answer, translation_list

        random_words, word = translate.get_random_word()
        u_id = message.from_user.id

        data.user_data[u_id] = [random_words, word]
        r_answer, translation_list = translate.translation(data.user_data[u_id][0], data.user_data[u_id][1])
        data.user_answer[u_id] = [translation_list, r_answer]

        msg = bot.send_message(message.from_user.id, text="Как переводится слово «{0}» 🧐".format(data.user_data[u_id][1]), reply_markup=buttons.user_data(message.from_user.id))
        bot.register_next_step_handler(msg, t_checking)
    elif (answer == "Стоп 🚫"):
        msg = bot.send_message(message.from_user.id, text="Эх, пока 😔", reply_markup=buttons.stop())
        bot.register_next_step_handler(msg, start)


# CHECK USER ANSWER
def t_checking(message):
    answer = message.text
    u_id = message.from_user.id

    if (answer == data.user_answer[u_id][1]):
        bot.send_message(message.from_user.id, "Верно, молодец! ❤️")
        msg = bot.send_message(message.from_user.id, text="Ещё? 🙃", reply_markup=buttons.repeat())
        bot.register_next_step_handler(msg, t_translation)
    elif (answer != data.user_answer[u_id][1]):
        bot.send_message(message.from_user.id, "Неверно, слово «{0}» переводится как «{1}» 😶‍🌫️".format(data.user_data[u_id][1], data.user_answer[u_id][1]))

        msg = bot.send_message(message.from_user.id, text="Ещё? 🙃", reply_markup=buttons.repeat())
        bot.register_next_step_handler(msg, t_translation)


bot.polling(none_stop=True)
