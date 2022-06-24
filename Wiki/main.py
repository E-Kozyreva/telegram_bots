import telebot
import wikipedia
from random import randint
from newspaper import Article

# TOKEN
bot = telebot.TeleBot("5058628758:AAGZabz49Yi-f6RRYeEm3_l6iwGBfKEi9ac");

# LANGUAGE
language = "ru"
wikipedia.set_lang(language)

# BUTTONS
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row("Привет 👋🏻")
keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.row("Найти статью в Wikipedia 🔍", "Случайная статья 🤔")
keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard3.row("Да ✅", "Нет ❌")

# START
@bot.message_handler(content_types=["text"])
def start(message):
    answer = message.text
    if answer == "Привет 👋🏻" or answer == "Привет" or answer == "привет":
        text = "Привет, выбери что-нибудь для себя 😉"
        msg = bot.send_message(message.from_user.id, text , reply_markup = keyboard2)
        bot.register_next_step_handler(msg, functions)
    elif answer == "/help":
        msg = bot.send_message(message.from_user.id, "Нажми на кнопку 👀" , reply_markup = keyboard1)
        bot.register_next_step_handler(msg, start)
    else:
        msg = bot.send_message(message.from_user.id, "Я тебя не понимаю 😔\nНапиши /help")
        bot.register_next_step_handler(msg, start)

# RESTART BOT FUNCTIONS
def restart(message):
    answer = message.text
    if answer == "Да ✅":
        text = "Рада, что ты хочешь ещё что-нибудь найти 😉"
        msg = bot.send_message(message.from_user.id, text , reply_markup = keyboard2)
        bot.register_next_step_handler(msg, functions)
    elif answer == "Нет ❌":
        msg = bot.send_message(message.from_user.id, "Жаль, была рада помочь, пока 🙂")
        bot.register_next_step_handler(msg, start)
    else:
        msg = bot.send_message(message.from_user.id, "Немного тебя не поняла, выбери что-то одно 😔")
        bot.register_next_step_handler(msg, restart)

# FUNCTIONS
def functions(message):
    answer = message.text
    if answer == "Найти статью в Wikipedia 🔍":
        text = "Окей, сейчас найду тебе статью 🙃\nОтправь мне слово, которое хочешь найти 😊"
        msg = bot.send_message(message.from_user.id, text)
        bot.register_next_step_handler(msg , user_word)
    elif answer == "Случайная статья 🤔":
        bot.send_message(message.from_user.id, "Сейчас что-нибудь найдём для тебя интересненькое 🙃")
        url ="https://ru.wikipedia.org/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%A1%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0"
        article = Article(url)
        article.download()
        article.parse()
        title_of_article = str(article.title)[:-11]

        python_page = wikipedia.page(title_of_article)

        page_url = python_page.url
        original_page_title = python_page.original_title
        page_summary = str(python_page.summary)

        text = '''📰 {0}\n\n{1}\n\n🌐 '''.format(original_page_title, page_summary)
        text += page_url

        bot.send_message(message.from_user.id, text)

        text = "Давай ещё что-нибудь узнаем? 😇"
        msg = bot.send_message(message.from_user.id, text , reply_markup = keyboard3)
        bot.register_next_step_handler(msg, restart)
    else:
        msg = bot.send_message(message.from_user.id, "Немного тебя не поняла, выбери что-то одно 😔")
        bot.register_next_step_handler(msg, functions)

# FIND STATE FOR USER
def user_word(message):
    generalizing_word_of_user = message.text
    generalizing_word = wikipedia.suggest(generalizing_word_of_user)

    if generalizing_word is not None:
        global possible_articles_1
        word = "Может ты хотел/ла найти {0}? 🤔".format(generalizing_word)
        bot.send_message(message.from_user.id, word)

        possible_articles_1 = list(wikipedia.search(generalizing_word))
        for page in possible_articles_1:
            print(page)

        number_of_article, text_wiki = 1, "Смогла найти такие статьи 🤗\n"
        for page in possible_articles_1:
            text_wiki += "{0} | {1}\n".format(number_of_article, page)
            number_of_article += 1

        bot.send_message(message.from_user.id, text_wiki)
        msg = bot.send_message(message.from_user.id, "Отправь мне номер статьи, которую хочешь прочитать 🙃")
        bot.register_next_step_handler(msg, find_article_1)
    else:
        global possible_articles_2
        possible_articles_2 = list(wikipedia.search(generalizing_word_of_user))

        number_of_article, text_wiki = 1, "Вот, что я смогла найти 🤗\n"
        for page in possible_articles_2:
            text_wiki += "{0} | {1}\n".format(number_of_article, page)
            number_of_article += 1

        bot.send_message(message.from_user.id, text_wiki)
        msg = bot.send_message(message.from_user.id, "Отправь мне номер статьи, которую хочешь прочитать 🙃")
        bot.register_next_step_handler(msg, find_article_2)

# FOR THE FIRST CONDITION
def find_article_1(message):
    article_number = message.text

    if int(article_number) in list(range(1, 10_000)):
        python_page = wikipedia.page(possible_articles_1[int(article_number) - 1])

        page_url = python_page.url
        original_page_title = python_page.original_title
        page_summary = str(python_page.summary)

        text = '''📰 {0}\n\n{1}\n\n🌐 '''.format(original_page_title, page_summary)
        text += page_url

        bot.send_message(message.from_user.id, text)
    else:
        bot.send_message(message.from_user.id, "Ты не ввёл/ла номер статьи, поэтому я выберу её за тебя 👿")
        article = randint(1, len(possible_articles_1))
        python_page = wikipedia.page(possible_articles_1[article])

        page_url = python_page.url
        original_page_title = python_page.original_title
        page_summary = str(python_page.summary)

        text = '''📰 {0}\n\n{1}\n\n🌐 '''.format(original_page_title, page_summary)
        text += page_url

        bot.send_message(message.from_user.id, text)

    text = "Давай ещё что-нибудь узнаем? 😇"
    msg = bot.send_message(message.from_user.id, text , reply_markup = keyboard3)
    bot.register_next_step_handler(msg, restart)

# FOR THE SECOND CONDITION
def find_article_2(message):
    article_number = message.text

    if int(article_number) in list(range(1, 10_000)):
        python_page = wikipedia.page(possible_articles_2[int(article_number) - 1])

        page_url = python_page.url
        original_page_title = python_page.original_title
        page_summary = str(python_page.summary)

        text = '''📰 {0}\n\n{1}\n\n🌐 '''.format(original_page_title, page_summary)
        text += page_url

        bot.send_message(message.from_user.id, text)
    else:
        bot.send_message(message.from_user.id, "Ты не ввёл/ла номер статьи, поэтому я выберу её за тебя 👿")
        article = randint(1, len(possible_articles_2))
        python_page = wikipedia.page(possible_articles_2[article])

        page_url = python_page.url
        original_page_title = python_page.original_title
        page_summary = str(python_page.summary)

        text = '''📰 {0}\n\n{1}\n\n🌐 '''.format(original_page_title, page_summary)
        text += page_url

        bot.send_message(message.from_user.id, text)


    text = "Давай ещё что-нибудь узнаем? 😇"
    msg = bot.send_message(message.from_user.id, text , reply_markup = keyboard3)
    bot.register_next_step_handler(msg, restart)

bot.polling(none_stop=True, interval=0)
