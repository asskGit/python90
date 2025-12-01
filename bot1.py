import telebot
from telebot import types

bot = telebot.TeleBot('7447585150:AAHS49IGT9SOXsEurFZXsgFaCrJms305uX8')


@bot.message_handler(commands=['start'])
def start(message):
    name = message.from_user.first_name
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('ПРИВЕТ')
    btn2 = types.KeyboardButton('Помощь')
    btn3 = types.KeyboardButton("Фото")

    kb.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, f'Hello {name}', reply_markup=kb)


@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == "ПРИВЕТ":
        bot.send_message(message.chat.id, 'тебе тоже привет')
    elif message.text == "Помощь":
        bot.send_message(message.chat.id, 'я пока умею только кнопки показать надо улучшить')

    elif message.text == "Фото":
        photo = open('photo.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, 'нажми на кнопку ниже')
bot.polling()

