import requests
import telebot
from telebot import types

api_token = '6001597679:AAGEEmHHwpmO4V3myDxf2KZBLyP6ytC7E5w'
bot = telebot.TeleBot(api_token)

url = "https://api.binance.com/api/v3/ticker/price?symbol="

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     f"Hello! This bot shows realtime cryptocurrencies prices.")

    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("BTC")
    item2=types.KeyboardButton("ETH")
    item3=types.KeyboardButton("BNB")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    bot.send_message(message.chat.id,'Choose the currency from the menu or type currency symbol (for example, ATOM)',
                     reply_markup=markup)

@bot.message_handler(content_types='text')
def get_price(message):
    r = requests.get(f'{url}{message.text}USDT')
    if r.status_code == 200:
        data = r.json()
        bot.send_message(message.chat.id,
                         text=f'Current {data["symbol"][:len(data["symbol"])-4]} price is ${round(float(data["price"]), 2)}')
    else:
        bot.send_message(message.chat.id, 'Problems on Binance API')

bot.polling(non_stop=True)
