from pyrogram import Client , filters, idle
from pyrogram.types import Message, ChatPermissions
import asyncio
import os

API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

#MONGO_URL = os.environ.get("MONGO_URL")


bot = Client(
    "Level" ,
    api_id = API_ID ,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)

Pic = "https://telegra.ph/file/59c987c5c838e973e8d3f.jpg"

@bot.on_message(filters.new_chat_members)
async def new(bot, message):
        im = message.from_user.id
        nm = message.from_user.mention
        unm = message.from_user.username
        msg = await message.reply_photo(photo=Pic, caption=f"👤{nm} [ @{unm} ] \n⚠️You won't be able to use MEDIA in group due to security purpose! \n**You need to be atleast 2 weeks here AND 100+ message sended**\n__Then you'll be authorised to send Media__")







@bot.on_message(filters.command("r"))
async def rel(bot, message):
    await message.reply_text("!bot reloaded")

@bot.on_message(filters.command("start") & filters.private)
async def start(bot, message):
    await message.reply_text("Pretty much nothing for Normies \n Join @Anime_Gaming_Chat_Global")

@bot.on_message(filters.command("settings") & filters.private)
async def settings(bot, message):
    uid = message.from_user.id
    mystic = await message.reply_text("Getting User Unique id...")
    await asyncio.sleep(1)
    await mystic.edit(f"👥: {uid}")
    await asyncio.sleep(1)
    await mystic.edit("UID Not Found In D.B.")
    await asyncio.sleep(1)
    await mystic.edit("⚠️Only Authorised Users Can use This command")

##okok 

bot.run() 
idle()
