from telegram import *
from telegram.ext import *
from requests import *
import random

updater = Updater(token="Token")
dispatcher = updater.dispatcher

def generate1():
    pw = ""
    for i in range(6):
        pw += str(random.choice(range(10)))
    return pw

def generate2():
    words = "abcdefghijklmnopqrstuvwxyz"
    pw = ""
    for i in range(6):
        pw += str(random.choice(words))
    return pw

def startCommand(update: Update, context: CallbackContext):
    buttons = [[KeyboardButton("Numeric Password")], [KeyboardButton("String Password")]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to my bot! Choose :",
                             reply_markup=ReplyKeyboardMarkup(buttons))


def messageHandler(update: Update, context: CallbackContext):
    if update.message.text == "Numeric Password":
        password = generate1()
        context.bot.send_message(chat_id=update.effective_chat.id, text=password)
    elif update.message.text == "String Password":
        password = generate2()
        context.bot.send_message(chat_id=update.effective_chat.id, text=password)
    else :
        context.bot.send_message(chat_id=update.effective_chat.id, text="Choose numeric or string")


dispatcher.add_handler(CommandHandler("start", startCommand))
dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))

updater.start_polling()
print("Bot is online ...")
