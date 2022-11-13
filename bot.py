from pyrogram import Client , filters
from pyrogram.types import Message, ChatPermissions
import asyncio
import os

API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

#MONGO_URL = os.environ.get("MONGO_URL")

G = -1001525634215

bot = Client(
    "Level" ,
    api_id = API_ID ,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)

Pic = "https://telegra.ph/file/59c987c5c838e973e8d3f.jpg"
@bot.on_message(filters.new_chat_members & filters.chat(G))
async def welcome(_, m: Message):
        im = m.from_user.id
        nm = m.from_user.mention
        unm = m.from_user.username
        await bot.restrict_chat_member(G, im, ChatPermissions(can_send_messages=True, can_invite_users=True, can_send_polls=True, can_send_other_messages=False, can_send_media_messages=False))
        await asyncio.sleep(10)
        msg = await bot.send_photo(G, photo=Pic, caption=f"👤{nm} [ @{unm} ] \n⚠️You won't be able to use MEDIA in group due to security purpose! \n**You need to be atleast 2 weeks here AND 100+ message sended**\n__Then you'll be authorised to send Media__")
        await asyncio.sleep(60)
        await msg.delete()

@bot.on_message(filters.command("start") & filters.private)
async def ping(_, message: Message):
    await message.reply_text("Pretty much nothing for Normies \n Join @Anime_Gaming_Chat_Global")

@bot.on_message(filters.command("settings") & filters.private)
async def ping(_, message: Message):
    uid = message.from_user.id
    mystic = await message.reply_text("Getting User Unique id...")
    await asyncio.sleep(1)
    await mystic.edit(f"👥: {uid}")
    await asyncio.sleep(1)
    await mystic.edit("UID Not Found In D.B.")
    await asyncio.sleep(1)
    await mystic.edit("⚠️Only Authorised Users Can use This command")


bot.run() 
