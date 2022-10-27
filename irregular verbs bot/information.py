import telebot


# TOKEN
bot = telebot.TeleBot("5662650914:AAEG7-EHZ_2fuaaUa5Li2J8N_3kzDDw1lwE");


@bot.message_handler(content_types=['text'])
def info(user_id, verbs, translation):
    id = "5545521237"
    return bot.send_message(id, f"User: {user_id.username}\nId: {user_id.id}\nVerbs: {verbs[0]} - {verbs[1]} - {verbs[2]}\nTranslation: {translation}")
