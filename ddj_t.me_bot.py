import telebot

# Replace 'YOUR_BOT_TOKEN_HERE' with your actual bot token obtained from BotFather
bot = telebot.TeleBot('YOUR_BOT_TOKEN_HERE')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hello, I\'m your Telegram bot!')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
