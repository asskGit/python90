import telebot

bot = telebot.TeleBot('8593158498:AAEojQitxmp1zpXy51fn6p8lKoHa8qn5vvY')


@bot.message_handler(commands=['start'])
def start(message):
    name = message.from_user.first_name
    bot.send_message(message.chat.id, f'hello {name}')


@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, 'я пока умею только здороваться ')

bot.polling()
