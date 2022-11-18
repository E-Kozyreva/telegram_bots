import telebot
import wikipedia


import data
import buttons
import random_article
import get_article


bot = telebot.TeleBot("5058628758:AAGZabz49Yi-f6RRYeEm3_l6iwGBfKEi9ac");


language = "ru"
wikipedia.set_lang(language)


@bot.message_handler(content_types=["text"])
def start(message):
    answer = message.text
    if answer == "Привет 👋🏻" or answer == "/start":
        text = "Привет, выбери что-нибудь для себя 😉"
        msg = bot.send_message(message.from_user.id, text , reply_markup = buttons.get_article())
        bot.register_next_step_handler(msg, functions)
    else:
        msg = bot.send_message(message.from_user.id, "Нажми на кнопку 👀" , reply_markup = buttons.get_hi())
        bot.register_next_step_handler(msg, start)


def restart(message):
    answer = message.text
    if answer == "Да ✅":
        text = "Рада, что ты хочешь ещё что-нибудь найти 😉"
        msg = bot.send_message(message.from_user.id, text , reply_markup = buttons.get_article())
        bot.register_next_step_handler(msg, functions)
    elif answer == "Нет ❌":
        msg = bot.send_message(message.from_user.id, "Жаль, была рада помочь, пока 🙂", reply_markup = buttons.get_hi())
        bot.register_next_step_handler(msg, start)
    else:
        msg = bot.send_message(message.from_user.id, "Немного тебя не поняла, выбери что-то одно 😔", reply_markup = buttons.get_new_function())
        bot.register_next_step_handler(msg, restart)


def functions(message):
    answer = message.text
    if answer == "Найти статью в Wikipedia 🔍":
        text = "Окей, сейчас найду тебе статью 🙃\nОтправь мне слово, которое хочешь найти 😊"
        msg = bot.send_message(message.from_user.id, text)
        bot.register_next_step_handler(msg , user_word)
    elif answer == "Случайная статья 🤔":
        bot.send_message(message.from_user.id, "Сейчас что-нибудь найдём для тебя интересненькое 🙃")
        bot.send_message(message.from_user.id, random_article.get_random_article(), parse_mode='Markdown')

        text = "Давай ещё что-нибудь узнаем? 😇"
        msg = bot.send_message(message.from_user.id, text , reply_markup = buttons.get_new_function())
        bot.register_next_step_handler(msg, restart)
    else:
        msg = bot.send_message(message.from_user.id, "Немного тебя не поняла, выбери что-то одно 😔", reply_markup = buttons.get_article())
        bot.register_next_step_handler(msg, functions)


def user_word(message):
    generalizing_word_of_user = message.text
    generalizing_word = wikipedia.suggest(generalizing_word_of_user)

    if generalizing_word != None:
        msg = bot.send_message(message.from_user.id, "Такой статьи к сожалению нет, давай найдём что-нибудь другое 🥺", reply_markup = buttons.get_article())
        bot.register_next_step_handler(msg, functions)
    else:
        text = "Смогла найти такие статьи, выбери одну из них 👀\n"
        bot.send_message(message.from_user.id, text + get_article.get_possible_articles(message.from_user.id, generalizing_word_of_user))
        msg = bot.send_message(message.from_user.id, "Отправь мне номер статьи, которую хочешь прочитать 😄")
        bot.register_next_step_handler(msg, user_article)


def user_article(message):
    answer = message.text
    possible_numbers = [str(n) for n in range(1, len(data.user_search[message.from_user.id]))]
    if answer in possible_numbers:
        text = get_article.get_article(data.user_search[message.from_user.id][int(answer) - 1])
        bot.send_message(message.from_user.id, text, parse_mode='Markdown')
        msg = bot.send_message(message.from_user.id, "Будем ещё что-нибудь ещё искать? 🤔", reply_markup = buttons.get_new_function())
        bot.register_next_step_handler(msg, restart)
    else:
        msg = bot.send_message(message.from_user.id, "Попробуй снова ☹️")
        bot.register_next_step_handler(msg, user_article)


bot.polling(none_stop=True, interval=0)