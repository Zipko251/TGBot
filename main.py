import telebot
from config import BOT_TOKEN, log, Open_Weather_key
import Weather

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start. Чтобы узнать, что я могу, напиши /help')
    log(message)

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Привет, я могу сказать тебе, какая сейчас погода в любом городе. Просто набери "погода %Твой город на английском%"')
    log(message)


@bot.message_handler(content_types=['text'])
def get_weather(message):
    if message.text.lower()[:7] == 'погода ':
        s_city_name = message.text[7:]
        log(message)
        city_id = Weather.get_city_id(s_city_name)
        conditions, temp = Weather.request_current_weather(city_id)
        bot.send_message(message.chat.id, 'Состояние погоды в городе {2}: {0} \nТемпература = {1}'.format(conditions,
                                                                                                        temp,
                                                                                                          s_city_name))


bot.polling(none_stop=True, interval=0)