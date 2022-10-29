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


@bot.on_message(filters.command("top2"))
async def rank(client, message):
    tl = level.find().sort("xp")
    dt1 = [x for x in level.find().sort('xp',pymongo.DESCENDING)][:10]
    texto = "🏆 TOP 10 PLAYERS 🏆\n\n"
    num = 0
    for x in dt1:
        users = await bot.get_users(x['USER_ID'])
        mention = "[" + users.first_name + "](tg://user?id=" + str(users.id) + ")" or users.first_name
        num += 1
        xp = xpnum["xp"]
        l = 0
        while True:
            if xp < ((125*(l**2))+(125*(l))):
                break
            l += 1
        xp -= ((125*((l-1)**2))+(125*(l-1)))
        fxp = f"{int(xp * 4)}/{int(2000 *((1/2) * l))}"
        texto += f"{num}》{mention} {l} ~ {fxp}\n"
        try:
           await message.reply_text(texto)
        except Exception as e:
           await message.reply_text(f"`{e}`")





@bot.on_message(filters.command("top1"))
async def rank(client, message):
    tl = level.find().sort("xp")
    dt1 = [x for x in level.find().sort('xp',pymongo.DESCENDING)][:10]
    await message.reply_text(dt1)

bot.run() 
