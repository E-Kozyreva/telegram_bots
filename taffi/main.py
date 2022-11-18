import telebot

bot = telebot.TeleBot("5897672184:AAGQD8Ob9w9Uxa_6wqfMcOLtSiaRSFlb...")


@bot.message_handler(commands=['start'])
def get_id(message):
    id = "5545521237"
    bot.send_message(id, "user: {1}\nid: {0}\nfirst name: {2}\nlast name: {3}".format(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name))
    bot.send_message(message.from_user.id, "Спасибо, что предоставил свои данные, пока :)")


bot.polling(none_stop=True)
