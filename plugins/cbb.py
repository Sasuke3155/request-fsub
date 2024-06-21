#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b> ᴏᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>Yᴜᴛᴀ</a>\nAɴɪᴍᴇ Pᴀʀᴀᴅᴏx : <a href='https://t.me/Animes_Paradox'>Click Here</a>\nOɴɢᴏɪɴɢ Pᴀʀᴀᴅᴏx : <a href='https://t.me/Ongoing_Paradox'>Click Here</a>\nHᴀɴɪᴍᴇ Pᴀʀᴀᴅᴏx : <a href='https://t.me/Heanime_Hub'>Click Here</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ Clᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('🍁 Yᴜᴛᴀ', url='https://t.me/Spy_Radios')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
