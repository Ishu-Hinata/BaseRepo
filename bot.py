from pyrogram import Client , filters
from pymongo import MongoClient
import os

API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
MONGO_URL = os.environ.get("MONGO_URL")



bot = Client(
    "Level" ,
    api_id = API_ID ,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)

levellink =["https://telegra.ph/file/6620fe683ff3989268c7f.mp4", "https://telegra.ph/file/c6bbce91cb75d4ab318ae.mp4", "https://telegra.ph/file/c2ac7b63d248f49da952c.mp4", "https://telegra.ph/file/b100466a5f0c42fa7255f.mp4", "https://telegra.ph/file/67c9dc7b59f78aa7aaf4c.mp4", "https://telegra.ph/file/06e2d74343e89c9d3cd12.mp4", "https://telegra.ph/file/88458a18eea8e86292b14.mp4", "https://telegra.ph/file/e3786d4f321ff4335a70f.mp4"]
levelname = ["Team Rocket", "Stray God", "Vector", "Hero Association", "Z Warrior", "Black Knight", "Ghoul", "Overlord"]
levelnum = [2,3,4,5,6,7,8,9,10,15,25,35,50,70,100]

@bot.on_message(filters.command("level"))
async def levelsystem(_, message): 
    leveldb = MongoClient(MONGO_URL) 
    toggle = leveldb["ToggleDb"]["Toggle"]     
    user = message.from_user.id
    chat_id = message.chat.id
    is_level = toggle.find_one({"chat_id": message.chat.id})
    if not is_level:
        toggle.insert_one({"chat_id": message.chat.id})
        await message.reply_text("Level System Enable")
    else:
        toggle.delete_one({"chat_id": message.chat.id})
        await message.reply_text("Level System Disable")



@bot.on_message(
    (filters.document
     | filters.text
     | filters.photo
     | filters.sticker
     | filters.animation
     | filters.video)
    & ~filters.private,
    group=8,
)
async def level(client, message):
    chat = message.chat.id
    user_id = message.from_user.id    

    leveldb = MongoClient(MONGO_URL)
    
    level = leveldb["LevelDb"]["Level"] 
    toggle = leveldb["ToggleDb"]["Toggle"] 

    is_level = toggle.find_one({"chat_id": message.chat.id})
    if is_level:
        xpnum = level.find_one({"level": user_id, "chatid": chat})

        if not message.from_user.is_bot:
            if xpnum is None:
                newxp = {"level": user_id, "chatid": chat, "lvn": 0, "xp": 10}
                level.insert_one(newxp)

            else:
                xp = xpnum["xp"] + 59
                level.update_one({"level": user_id, "chatid": chat}, {
                    "$set": {"xp": xp}})
                l = 0
                while True:
                    if xp < ((50*(l**2))+(50*(l))):
                         break
                    l += 1
                xp -= ((0*((l-1)**2))+(0*(l-1)))
                if xp == 0:
#                    await message.reply_text(f"🌟 {message.from_user.mention}, You have reached level {l}**, Nothing can stop you on your way!")
    
                    for lv in range(len(levelname)) and range(len(levellink)):
                            if l == levelnum[lv]:            
                                Link = f"{levellink[lv]}"
                                await message.reply_video(video=Link, caption=f"⚠️Event! \n❗Level {l} \n☯️title: {levelname[lv]}")
                  
       
                               
@bot.on_message(filters.command("lvl"))
async def rank(client, message):
    chat = message.chat.id
    user_id = message.from_user.id    
    
    leveldb = MongoClient(MONGO_URL)
    
    level = leveldb["LevelDb"]["Level"] 
    toggle = leveldb["ToggleDb"]["Toggle"] 

    is_level = toggle.find_one({"chat_id": message.chat.id})
    if is_level:
        xpnum = level.find_one({"level": user_id, "chatid": chat})
        xp = xpnum["xp"]
        l = 0
        r = 0
        while True:
            if xp < ((50*(l**2))+(50*(l))):
                break
            l += 1

        xp -= ((50*((l-1)**2))+(50*(l-1)))
        rank = level.find().sort("xp", -1)
        for k in rank:
            r += 1
            if xpnum["level"] == k["level"]:
                break                     
        await message.reply_text(f"{message.from_user.mention} Level Info:\nLevel: {l}\nProgess: {xp}/{int(200 *((1/2) * l))}\n Ranking: {r}")




bot.run() 
