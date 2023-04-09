import telebot
from config import TOKEN
from telebot import types

bot = telebot.TeleBot(TOKEN)
print("[~] Start bot...")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Кнопка 1")
    btn2 = types.KeyboardButton("Кнопка 2")
    btn3 = types.KeyboardButton("Кнопка 3")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.from_user.id, "Привет, выбери кнопку :)", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Кнопка 1":
        bot.send_message(message.from_user.id, "Это кнопка 1 :)")
    elif message.text == "Кнопка 2":
        bot.send_message(message.from_user.id, "Это кнопка 2 :)")
    elif message.text == "Кнопка 3":
        bot.send_message(message.from_user.id, "Это кнопка 3 :)")
    else:
        bot.send_message(message.from_user.id, "Такой кнопки нет :(")


bot.polling(none_stop=True, interval=0)

# None_stop: True / False (по умолчанию False) - не прекращать опрос при получении ошибки от серверов Telegram
# interval: True / False (по умолчанию False) - интервал между запросами на опрос.
# Изменение этого параметра снижает время отклика бота.
# Timeout: целое число (по умолчанию 20) - Тайм-аут в секундах для длительного опроса
