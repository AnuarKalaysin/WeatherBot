import telebot
import requests
import json

bot = telebot.TeleBot('7031458326:AAGaBi-lx5SCwTrUkwNqhNCzExYJfdfY7m8')
API = 'd2b82ae8ebe896d979d682f13b06063c'

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f"Hello, {message.from_user.first_name}! Just send me the city")

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'Write me <u>@AnuarKalaysin</u>', parse_mode='Html')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric")

    if city == "hello":
        bot.reply_to(message, f"Hello, {message.from_user.first_name}!")
        return

    if res.status_code == 200:
        data = json.loads(res.text)
        bot.reply_to(message, f"{data['weather'][0]['main']}\n"
                              f"The current temperature: {data['main']['temp']}°C\n"
                              f"Feels like: {data['main']['feels_like']}°C ")

    else:
        bot.reply_to(message, f"This city doesn't exist!")

bot.polling(non_stop=True)