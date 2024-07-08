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
            text = f"<b> ᴏᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>❤️</a>\nᴀɴɪᴍᴇ sʜʀɪɴᴇ ⛩️ : <a href='https://t.me/Animes_Shrine'>ᴊᴏɪɴ ɴᴏᴡ</a>\nᴏɴɢᴏɪɴɢ sʜʀɪɴᴇ ⛩️: <a href='https://t.me/Ongoing_Shrine'>ᴊᴏɪɴ ɴᴏᴡ</a>\nᴄᴜʟᴛᴜʀᴇᴅ sʜʀɪɴᴇ ⛩️ : <a href='https://t.me/Cultured_Shrine'>ᴊᴏɪɴ ɴᴏᴡ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('🍁 ᴛᴀɴᴊɪʀᴏ', url='https://t.me/KamadoSen')
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
