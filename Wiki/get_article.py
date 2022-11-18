import wikipedia
import data


def get_articles(user_id, generalizing_word):
    possible_articles = list(wikipedia.search(generalizing_word))

    number_of_article, text_wiki = 1, ""
    for page in possible_articles:
        text_wiki += "{0}. {1}\n".format(number_of_article, page)
        number_of_article += 1

    data.user_search[user_id] = possible_articles
    return text_wiki