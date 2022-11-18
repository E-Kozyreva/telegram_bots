import wikipedia


def get_word_is_not_none(generalizing_word):
    global possible_articles_1

    possible_articles_1 = list(wikipedia.search(generalizing_word))
    for page in possible_articles_1:
        print(page)

    number_of_article, text_wiki = 1, "Смогла найти такие статьи 🤗\n"
    for page in possible_articles_1:
        text_wiki += "{0} | {1}\n".format(number_of_article, page)
        number_of_article += 1



def get_word_is_none(generalizing_word):
    global possible_articles_2
    possible_articles_2 = list(wikipedia.search(generalizing_word))

    number_of_article, text_wiki = 1, "Вот, что я смогла найти 🤗\n"
    for page in possible_articles_2:
        text_wiki += "{0} | {1}\n".format(number_of_article, page)
        number_of_article += 1