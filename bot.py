from pyrogram import Client , filters

from pymongo import MongoClient
import os
from sex import*


API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

MONGO_URL = os.environ.get("MONGO_URL")

G = -1001686630791

bot = Client(
    "Level" ,
    api_id = API_ID ,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)

@bot.on_message(filters.command("test"))
async def rank(client, message):
    await message.reply_text(f"🎆Added")

#all codes deleted

# repo only fir testing

#   @lord_DSP_3

bot.run() 
