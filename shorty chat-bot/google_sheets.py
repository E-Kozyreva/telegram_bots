import gspread
import ast

gc = gspread.service_account(filename='english-368919-03231f9f1f0c.json')
sht = gc.open_by_url('https://docs.google.com/spreadsheets/d/1iblSYSACiatXwvXqx4oCrbtqqappiS4oynNZjNb8yTE/edit#gid=0')
worksheet = sht.sheet1


def get_individual_reading(user):
    individual_reading = worksheet.col_values(1)
    individual_reading["user"] = user
    return individual_reading


def get_test_your_english(user):
    test_your_english = worksheet.col_values(2)
    test_your_english["user"] = user
    return test_your_english


def get_english_for_math(user):
    english_for_math = worksheet.col_values(3)
    english_for_math["user"] = user
    return english_for_math

def get_english_language_texts(user):
    english_language_texts = worksheet.col_values(4)
    english_language_texts["user"] = user
    return english_language_texts
