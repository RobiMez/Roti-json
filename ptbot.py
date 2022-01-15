import json
import random
import os
import dotenv
from telegram.ext import Updater

dotenv.load_dotenv('.env')
TOKEN = os.getenv('TOKEN')

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi there , Im random Roti ( Rules Of The Internet ) bot , send /rroti to get a random rule .\n\n Made by github.com/robimez")
    
def rroti(update, context):
    with open('./rules_of_the_internet.json', encoding="utf8") as f:
        data = json.load(f)
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Rule {random.choice(list(data))} : {data[random.choice(list(data))]}")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('rroti', rroti)
dispatcher.add_handler(start_handler)

print('Bot started.')
updater.start_polling()




