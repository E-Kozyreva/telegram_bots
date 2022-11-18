import wikipedia
from random import randint
from newspaper import Article

# LANGUAGE
language = "ru"
wikipedia.set_lang(language)


def get_random_article():
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

    return text
