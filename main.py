import telebot


bot = telebot.TeleBot('6241547749:AAHnvFfdq9unR-HxVzzxF2EK5O02DVvsdhY')


@bot.message_handler(commands=['start'])             # содержит список команд
def main(message):
    bot.send_message(message.chat.id, 'Привет')      # вывод сообщения


@bot.message_handler(commands=['hello'])
def main(message):
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name} {message.from_user.last_name}')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, f'')


@bot.message_handler()                              # на вход обычный текст, не команды, в конец списка    
def main(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')
    




bot.infinity_polling()                              # будет работать постоянно