import telebot
import webbrowser
from telebot import types


bot = telebot.TeleBot('6241547749:AAHnvFfdq9unR-HxVzzxF2EK5O02DVvsdhY')


@bot.message_handler(commands=['site', 'website', 'page'])
def main(message):
    webbrowser.open('https://github.com/imartov')       # переходит по указанному url-адресу


@bot.message_handler(commands=['start'])             # содержит список команд
def main(message):
    bot.send_message(message.chat.id, 'Привет')      # вывод сообщения


@bot.message_handler(content_types=['photo'])       # принимает файл
def get_file(message):
    markup = types.InlineKeyboardMarkup()                                                               # добавляется кнопка к сообщению
    markup.add(types.InlineKeyboardButton('Перейти на сайт', url='https://github.com/imartov'))
    bot.reply_to(message.chat.id, 'Какое красивое фото', reply_markup=markup)


@bot.message_handler(commands=['hello'])
def main(message):
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name} {message.from_user.last_name}')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, f'help')


@bot.message_handler()                              # на вход обычный текст, не команды, в конец списка    
def main(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')    # ответ на предыдущее сообщение (закрепление)


'''
Существует два вида кнопок:
1. Inline - отображаются около сообщения
2. Меню - отображаются в меню
'''


    

bot.infinity_polling()                              # будет работать постоянно