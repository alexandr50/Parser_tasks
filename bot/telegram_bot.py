import os
import time
from pathlib import Path

import telebot
from dotenv import load_dotenv
from telebot import types

from classes.database import DBManager
from schedule import params

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / '.env')

bot = telebot.TeleBot(os.getenv('bot_token'))

db = DBManager('parser_db', params=params)


# @bot.message_handler(commands=['button'])
# def button_message(message):
#
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     item = types.KeyboardButton("Кнопка")
#     markup.add(item)
#     bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)


@bot.message_handler(commands=['theme'])
def start_bot_theme(message):
    """Вывод меню для фильрации по теме"""

    lst = db.get_all_theme()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for item in lst:
        markup.add(types.KeyboardButton(item[0]))
    if message.chat.type == 'private':
        bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}, chose the theme!',
                         reply_markup=markup)
    bot.register_next_step_handler(message, print_query_for_theme)


@bot.message_handler(chat_types=['text'])
def print_query_for_theme(message):
    """Вывод данных согласнр выбранному пункту"""

    theme = message.text
    result_data = db.get_data_for_telegramm_theme(theme)
    for item in result_data:
        bot.send_message(message.chat.id,
                         f'''Number: {item[0]}, Name: {item[1]}, Theme: {item[2]},
                           Rating: {item[3]}, Count_solutions: {item[4]}''')
        time.sleep(0.5)


@bot.message_handler(commands=['rating'])
def start_bot_rating(message):
    """Вывод меню для фильрации по рейтингу"""

    lst = db.get_all_rating()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for item in lst:
        markup.add(types.KeyboardButton(str(item[0])))
    if message.chat.type == 'private':
        bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}, chose the rating!',
                         reply_markup=markup)
    bot.register_next_step_handler(message, print_query_for_rating)


@bot.message_handler(chat_types=['text'])
def print_query_for_rating(message):
    """Вывод данных согласнр выбранному пункту"""

    rating = int(message.text)
    result_data = db.get_data_for_telegramm_rating(rating)
    for item in result_data:
        bot.send_message(message.chat.id,
                         f'Number: {item[0]}, Name: {item[1]}, Theme: {item[2]}, '
                         f'Rating: {item[3]}, Count_solutions: {item[4]}')
        time.sleep(0.5)


bot.infinity_polling(none_stop=True)
