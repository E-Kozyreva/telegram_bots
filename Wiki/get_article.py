import wikipedia
from random import randint
from newspaper import Article


import data


language = "ru"
wikipedia.set_lang(language)


def get_possible_articles(user_id, generalizing_word):
    possible_articles = list(wikipedia.search(generalizing_word))

    number_of_article, text_wiki = 1, ""
    for page in possible_articles:
        text_wiki += "{0}. {1}\n".format(number_of_article, page)
        number_of_article += 1

    data.user_search[user_id] = possible_articles
    return text_wiki


def get_article(title_of_article):
    python_page = wikipedia.page(title_of_article)

    page_url = python_page.url.replace('\n',"")
    original_page_title = python_page.original_title.replace('\n',"")
    page_summary = str(python_page.summary).replace('\n',"")

    text = '''📰 {0}\n\n{1}\n\n{2}'''.format(original_page_title, page_summary, f'[Подробнее...]({page_url})')
    return text