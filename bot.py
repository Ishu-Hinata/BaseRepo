from pyrogram import Client , filters, idle
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
        await bot.restrict_chat_member(message.chat.id, im, ChatPermissions(can_send_messages=True, can_invite_users=True, can_send_polls=True, can_send_other_messages=False, can_send_media_messages=False))
        msg = await message.reply_photo(photo=Pic, caption=f"👤{nm} [ @{unm} ] \n⚠️You won't be able to use MEDIA in group due to security purpose! \n**You need to be atleast 2 weeks here AND 100+ message sended**\n__Then you'll be authorised to send Media__")


#REMOVEBG_API = "KMFFqrBYBocDHBYbz8Gwa2np"
#UNSCREEN_API = "zhLmhhqxbYrKbXrsw5bbnKeo"

@bot.on_message(filters.private & (filters.photo | filters.video | filters.document))
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
        await update.reply_sticker(
            sticker=new_file_name
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

##

bot.run() 
idle()
