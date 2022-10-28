from deep_translator import GoogleTranslator
import random
import words


# GENERATE RANDOM WORDS
def get_random_word():
    random_words = random.choices(words.words_list, k=4)
    word = random.choice(random_words).lower()
    return random_words, word


# TRANSLATE WORDS
def translation(words, word):
    r_answer = GoogleTranslator(source='en', target='ru').translate(word).lower()
    w1 = GoogleTranslator(source='en', target='ru').translate(words[0]).lower()
    w2 = GoogleTranslator(source='en', target='ru').translate(words[1]).lower()
    w3 = GoogleTranslator(source='en', target='ru').translate(words[2]).lower()
    w4 = GoogleTranslator(source='en', target='ru').translate(words[3]).lower()
    translation_list = [w1, w2, w3, w4]
    return r_answer, translation_list
