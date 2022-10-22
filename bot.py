from pyrogram import Client , filters
import pymongo
from pymongo import MongoClient
import os

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

leveldb = MongoClient(MONGO_URL)
level = leveldb["LEVEL"]["mem_LVL"]

@bot.on_message(filters.command("top1"))
async def rank(client, message):
    tl = level.find().sort("xp")
    dt1 = [x for x in level.find().sort('xp',pymongo.DESCENDING)][:10]
#    for x in dt1:
#        users = await bot.get_users(x['USER_ID'])
    await message.reply_text(dt1)

@bot.on_message(filters.command("top2"))
async def rank(client, message):
    tl = level.find().sort("xp")
    dt1 = [x for x in level.find().sort('xp',pymongo.DESCENDING)][:10]
    texto = "🏆 TOP 25 PLAYERS 🏆"
    num = 0
    for x in dt1:
        users = await bot.get_users(x['USER_ID'])
        if users.mention:
           data = users.mention
        else:
           data = x['USER_ID']
           num =+ 1
           texto += f"{num}》{data}\n"
           await message.reply_text(texto)

#@bot.on_message(filters.command("top3", configg.PREFIXES))
#async def rank(client, message):
#    tl = level.find().sort('xp')
#    dt1 = [x for x in level.find().sort('xp',pymongo.DESCENDING)][:10]
#    texto = "🏆 TOP 10 PLAYERS 🏆"
#    num = 0
#    for x in dt1:
#        num += 1
#        users = await bot.get_users(x['USER_ID'])
#        if users.mention:
#           data = users.mention
#        else:
#           data = x['USER_ID']
#           texto += f"{num}》{data}\n"
#           await message.reply_text(texto)




#

# repo only for testing

#

bot.run() 
