from pyrogram import Client, filters
from pyrogram.types import Message
from nexichat import nexichat

@Client.on_message(filters.command("start"))
async def start_message(client: Client, message: Message):
    await message.reply_text(
        f"𝙃𝙚𝙡𝙡𝙤 {message.from_user.first_name}! 👋\n\n"
        "𝙃𝙚𝙮 , 𝙄 𝙖𝙢 𝙔𝙤𝙪𝙧 𝙍𝙚𝙖𝙘𝙩𝙞𝙤𝙣 𝙃𝙤𝙨𝙩𝙚𝙧 𝘽𝙤𝙩 𝙃𝙤𝙨𝙩 𝙔𝙤𝙪𝙧 𝙊𝙬𝙣 𝘽𝙤𝙩 𝙁𝙤𝙧 𝙁𝙧𝙚𝙚\n\n"
        "𝘼𝙙𝙙 𝙢𝙚 𝙩𝙤 𝙮𝙤𝙪𝙧 𝘾𝙝𝙖𝙣𝙣𝙚𝙡𝙨 𝙛𝙤𝙧 𝙛𝙧𝙚𝙚 𝙍𝙚𝙖𝙘𝙩𝙞𝙤𝙣𝙨 𝙑𝙞𝙨𝙞𝙩 [𝙏𝙝𝙚 𝘽𝙤𝙩𝙨 𝙃𝙪𝙗](t.me/TheBotsHub)! 🚀 \n\n"
        "**𝙈𝙖𝙠𝙚 𝙔𝙤𝙪𝙧 𝙊𝙬𝙣 𝘽𝙤𝙩 𝘽𝙮 /host[😁](https://graph.org/file/66cb6ec40eea5c4670118.jpg)**"
    )
