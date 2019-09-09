import telebot
from config import TOKEN, log

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')
    log(message)


@bot.message_handler(content_types=['text'])
def random_message(message):
    if message.text.lower() == 'погода':
        bot.send_message(message.chat.id, 'Вы написали погода')


bot.polling(none_stop=True, interval=0)