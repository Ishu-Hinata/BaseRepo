from pyrogram import Client , filters

from pymongo import MongoClient
import os
from sex import*
from pyrogram.types import Message

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

levellink =["https://telegra.ph/file/6620fe683ff3989268c7f.mp4", "https://telegra.ph/file/c6bbce91cb75d4ab318ae.mp4", "https://telegra.ph/file/c2ac7b63d248f49da952c.mp4", "https://telegra.ph/file/b100466a5f0c42fa7255f.mp4", "https://telegra.ph/file/67c9dc7b59f78aa7aaf4c.mp4", "https://telegra.ph/file/06e2d74343e89c9d3cd12.mp4", "https://telegra.ph/file/88458a18eea8e86292b14.mp4", "https://telegra.ph/file/e3786d4f321ff4335a70f.mp4"]
levelname = ["Team Rocket", "Stray God", "Vector", "Hero Association", "Z Warrior", "Black Knight", "Ghoul", "Overlord"]
levelnum = [2,3,4,5,6,7,8,9,10,15,25,35,50,70,100]

@bot.on_message(
    (filters.document
     | filters.text
     | filters.photo
     | filters.sticker
     | filters.animation
     | filters.video)
    & filters.chat(G),
    group=1,
)
async def level(client, message):
    user_id = message.from_user.id
    rtxt = "ㅤ"
    leveldb = MongoClient(MONGO_URL)
    level = leveldb["LEVEL"]["mem_LVL"]
    xpnum = level.find_one({"USER_ID": user_id})
    if not message.from_user.is_bot:
        if xpnum is None:
            newxp = {"USER_ID": user_id, "xp": 10, "Repu": 0, "trank": rtxt}
            level.insert_one(newxp)
        else:
            xp = xpnum["xp"] + 1
            level.update_one({"USER_ID": user_id}, {
                "$set": {"xp": xp}})
            l = 0
            while True:
                if xp < ((125*(l**2))+(125*(l))):
                    break
                l += 1
            xp -= ((125*((l-1)**2))+(125*(l-1)))
            if xp == 0:
                for lv in range(len(levelname)) and range(len(levellink)):
                    if l == levelnum[lv]:
                        Link = f"{levellink[lv]}"
                        await message.reply_video(video=Link, caption=f"⚠️Event!  \n\n❗Level {l} \n\n☯️title: {levelname[lv]}")


async def get_user(user, already=False):
    user = await bot.get_users(user)
    mention = user.mention
    photo_id = user.photo.big_file_id if user.photo else None
    user_id = user.id

    leveldb = MongoClient(MONGO_URL)
    level = leveldb["LEVEL"]["mem_LVL"]
    xpnum = level.find_one({"USER_ID": user_id})
    xp = xpnum["xp"]
    rp = xpnum["Repu"]
    cs = xpnum["trank"]
    l = 0
    r = 0
    while True:
        if xp < ((125*(l**2))+(125*(l))):
            break
        l += 1
    xp -= ((125*((l-1)**2))+(125*(l-1)))
    rank = level.find().sort("xp", -1)
    fxp = f"{int(xp * 4)}/{int(2000 *((1/2) * l))}"
    for k in rank:
        r += 1
        if xpnum["level"] == k["level"]:
            break 
    caption = f"""
    ╔════༻sᴛᴀᴛᴜs༺════╗
       𝚃𝙸𝚃𝙻𝙴:  {cs}
💠 {mention}
   𝘙𝘦𝘱𝘶𝘵𝘢𝘵𝘪𝘰𝘯: {rp} ✰
     
     𝙇𝙀𝙑𝙀𝙇: {l}  ʀᴀɴᴋ: {r}
     ᴇxᴘ:  {fxp}
"""
    return [caption, photo_id]

@bot.on_message(filters.command("iii"))
async def info_func(_, message: Message):
    user = message.from_user.id
    m = await message.reply_text("🦋")
    try:
        info_caption, photo_id = await get_user(user)
    except Exception as e:
        return await m.edit(str(e))
    if not photo_id:
        return await m.edit(info_caption, disable_web_page_preview=True)
    photo = await bot.download_media(photo_id)
    await message.reply_document(document=photo, caption=info_caption, quote=False)
    await m.delete()
    os.remove(photo)


bot.run() 
