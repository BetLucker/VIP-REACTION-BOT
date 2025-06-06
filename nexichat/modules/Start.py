from pyrogram import Client, filters
from pyrogram.types import Message
from nexichat import nexichat

@nexichat.on_message(filters.command("start"))
async def start_message(client: Client, message: Message):
    await message.reply_text(
        f"ʏᴏᴏ {message.from_user.first_name}! 👋\n\n"
        "ɪ ᴀᴍ ʀᴇᴀᴄᴛɪᴏɴ ᴄʟᴏɴᴇʀ ʙᴏᴛ! ɪ ᴡɪʟʟ ʀᴇᴀᴄᴛ ᴛᴏ ᴇᴠᴇʀʏ ᴍᴇssᴀɢᴇ sᴇɴᴅ ɪɴ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ, channels, and private chats with a 👍 emoji.\n\n"
        "ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ sᴇᴇ ᴍʏ ʀᴇᴀʟ ᴘᴏᴡᴇʀ! [🚀](https://files.catbox.moe/ydls1x.jpg)\n\n"
        "**ᴡᴀɴᴛ ᴛᴏ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ /clone**"
        "** ➳ ᴘᴏᴡᴇʀᴇᴅ ʙʏ [ʟᴇɢɪʏ ɴᴇᴛᴡᴏʀᴍ](t.me/TheBotsHub)**"
        "** ➳ ᴀʟʟ ᴜᴘᴅᴀᴛᴇs [ʟᴇɢɪʏ ᴜᴘᴅᴀᴛᴇs](t.me/Nirvox)**"
    )
    
