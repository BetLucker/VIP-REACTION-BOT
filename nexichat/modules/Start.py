from pyrogram import Client, filters
from pyrogram.types import Message
from nexichat import nexichat

@nexichat.on_message(filters.command("start","on"))
async def start_message(client: Client, message: Message):
    await message.reply_text(
        f"👋 Welcome to the Reaction Bot! 🎉\n\n"
        "Hey there! I'm here to help you create your very own reaction bot in just a few simple steps. If you're ready to unleash your creativity and bring some fun to your server, you've come to the right place!.\n\n"
        "✨ Get Started: To clone your very own reaction bot, just type /clone and your bot token. It's that easy! [🚀](https://files.catbox.moe/ydls1x.jpg)\n\n"
        "**💡 Need Help? If you have any questions or need assistance, feel free to ask. I'm here to help!
**"
        "**Now that you're all set up, let’s dive in and start creating some amazing reactions together!**"
        "** 🦇 Let’s get started and have some fun! ☑️**"
    )
    
