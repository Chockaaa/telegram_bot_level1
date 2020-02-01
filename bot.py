# Imports
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import zodiac

# Variables
updater = Updater(token='1088724944:AAGxVJWykfDkTEO1R2k3L_QgM-7t9-REyEw', use_context=True)
dispatcher = updater.dispatcher

# Functions
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to horoscope identifier")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def setDate(update, context):
    ddmm=update.message.text[9:]
    dd=int(ddmm[:2])
    mm=int(ddmm[2:])
    sign=zodiac.getSign(dd,mm)
    context.bot.send_message(chat_id=update.effective_chat.id, text="You are sign is "+sign)

def horoscope(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Result")

# Main
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)


date_handler = CommandHandler('setDate', setDate)
dispatcher.add_handler(date_handler)

horo_handler = CommandHandler('horoscope', horoscope)
dispatcher.add_handler(horo_handler)

updater.start_polling()
print("Bot is working")
