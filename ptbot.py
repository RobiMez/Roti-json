import json
import random

from telegram.ext import Updater
updater = Updater(token='2037773235:AAFuGYes7IRVFKHGMOe_Nhz7yeyIi2VHLj4', use_context=True)

dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi there , Im random Roti ( Rules Of The Internet ) bot , send /rroti to get a random rule .\n\n Made by Robi")
    
def rroti(update, context):
    with open('./roti.json', encoding="utf8") as f:
        data = json.load(f)
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Rule {random.choice(list(data))} : {data[random.choice(list(data))]}")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('rroti', rroti)
dispatcher.add_handler(start_handler)


updater.start_polling()




