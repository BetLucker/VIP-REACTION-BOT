import logging
import os
from pyrogram.enums import ParseMode
from pyrogram import Client, filters
from pyrogram.errors import PeerIdInvalid
from pyrogram.errors.exceptions.bad_request_400 import AccessTokenExpired, AccessTokenInvalid
import config
from nexichat.mplugin.helpers import is_owner
from config import API_HASH, API_ID, OWNER_ID
from nexichat import CLONE_OWNERS
from nexichat import nexichat as app, save_clonebot_owner
from nexichat import db as mongodb, nexichat

CLONES = set()
cloneownerdb = mongodb.cloneownerdb
clonebotdb = mongodb.clonebotdb


@Client.on_message(filters.command(["host", "deploy"]))
async def clone_txt(client, message):
    if len(message.command) > 1:
        bot_token = message.text.split("/clone", 1)[1].strip()
        mi = await message.reply_text("Please wait while I check the bot token.")
        try:
            ai = Client(bot_token, API_ID, API_HASH, bot_token=bot_token, plugins=dict(root="nexichat/mplugin"))
            await ai.start()
            bot = await ai.get_me()
            bot_id = bot.id
            user_id = message.from_user.id
            await save_clonebot_owner(bot_id, user_id)
            await ai.set_bot_commands([
                    BotCommand("start", "Start the bot"),
                    BotCommand("help", "Get the help menu"),
                    BotCommand("clone", "Make your own chatbot"),
                    BotCommand("ping", "Check if the bot is alive or dead"),
                    BotCommand("id", "Get users user_id"),
                    BotCommand("stats", "Check bot stats"),
                    BotCommand("gcast", "Broadcast any message to groups/users"),
                    BotCommand("repo", "Get chatbot source code"),
                ])
        except (AccessTokenExpired, AccessTokenInvalid):
            await mi.edit_text("**Invalid bot token. Please provide a valid one.**")
            return
        except Exception as e:
            cloned_bot = await clonebotdb.find_one({"token": bot_token})
            if cloned_bot:
                await mi.edit_text("**🤖 𝗬𝗼𝘂𝗿 𝗕𝗼𝘁 𝗶𝘀 𝗛𝗼𝘀𝘁𝗲𝗱 𝗩𝗶𝘀𝗶𝘁 @TheBotsHub ✅**")
                return

        await mi.edit_text("**𝙃𝙤𝙨𝙩𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘽𝙤𝙩 𝙤𝙣 𝙤𝙪𝙧 𝙎𝙚𝙧𝙫𝙚𝙧....**")
        try:
            details = {
                "bot_id": bot.id,
                "is_bot": True,
                "user_id": user_id,
                "name": bot.first_name,
                "token": bot_token,
                "username": bot.username,
            }
            cloned_bots = clonebotdb.find()
            cloned_bots_list = await cloned_bots.to_list(length=None)
            total_clones = len(cloned_bots_list)
            await clonebotdb.insert_one(details)
            CLONES.add(bot.id)
            
            await app.send_message(
                int(OWNER_ID), f"**#New_Clone**\n\n**Bot:- @{bot.username}**\n\n**Details:-**\n{details}\n\n**Total Cloned:-** {total_clones}"
            )

            await mi.edit_text(
                f"**Bot @{bot.username} has been successfully cloned and started ✅.**\n**Remove clone by :- /delidclone**\n**Check all cloned bot list by:- /idcloned**"
            )
        except PeerIdInvalid as e:
            await mi.edit_text(f"**Your bot successfully cloned👍**\n**You can check by /cloned**\n\n**But please start me (@{nexichat.username}) From owner id**")
        
        except BaseException as e:
            logging.exception("𝘿𝙚𝙩𝙚𝙘𝙩𝙚𝙙 𝙀𝙧𝙧𝙤𝙧 𝙒𝙝𝙞𝙡𝙚 𝙃𝙤𝙨𝙩𝙞𝙣𝙜.")
            await mi.edit_text(
                f"⚠️ <b>Error:</b>\n\n<code>{e}</code>\n\n**Forward this message to @THE_VIP_BOY_OP for assistance**"
            )
    else:
        await message.reply_text("**𝙂𝙞𝙫𝙚 𝘽𝙤𝙩𝙏𝙤𝙠𝙚𝙣 𝘼𝙛𝙩𝙚𝙧 /𝙝𝙤𝙨𝙩 𝙛𝙧𝙤𝙢 @Botfather.**\n\n**Example:** `/clone bot token paste here`")


@Client.on_message(filters.command("hosted"))
async def list_cloned_bots(client, message):
    try:
        cloned_bots = clonebotdb.find()
        cloned_bots_list = await cloned_bots.to_list(length=None)
        if not cloned_bots_list:
            await message.reply_text("No bots have been cloned yet.")
            return
        total_clones = len(cloned_bots_list)
        text = f"**Total Cloned Bots:** {total_clones}\n\n"
        for bot in cloned_bots_list:
            text += f"**Bot ID:** `{bot['bot_id']}`\n"
            text += f"**Bot Name:** {bot['name']}\n"
            text += f"**Bot Username:** @{bot['username']}\n\n"
        await message.reply_text(text)
    except Exception as e:
        logging.exception(e)
        await message.reply_text("**An error occurred while listing cloned bots.**")

@Client.on_message(
    filters.command(["deletehosted", "delhosted", "delhost", "deletehost", "removehost", "cancelclone"])
)
async def delete_cloned_bot(client, message):
    try:
        if len(message.command) < 2:
            await message.reply_text("**Provide Bot Token after /delhost Command from @Botfather.**\n\n**Example:** `/delclone bot token paste here`")
            return

        bot_token = " ".join(message.command[1:])
        ok = await message.reply_text("**Checking the bot token...**")

        cloned_bot = await clonebotdb.find_one({"token": bot_token})
        if cloned_bot:
            await clonebotdb.delete_one({"token": bot_token})
            
            await ok.edit_text(
                f"**🤖 your cloned bot has been removed from my database ✅**\n**🔄 Kindly revoke your bot token from @botfather otherwise your bot will stop when @{app.username} will restart ☠️**"
            )
        else:
            await message.reply_text("**⚠️ The provided bot token is not in the hosted list.**")
    except Exception as e:
        await message.reply_text(f"**An error occurred while deleting the cloned bot:** {e}")
        logging.exception(e)


@Client.on_message(filters.command("delallclone") & filters.user(int(OWNER_ID)))
async def delete_all_cloned_bots(client, message):
    try:
        a = await message.reply_text("**Deleting all cloned bots...**")
        await clonebotdb.delete_many({})
        CLONES.clear()
        await a.edit_text("**All cloned bots have been deleted successfully ✅**")
    except Exception as e:
        await a.edit_text(f"**An error occurred while deleting all cloned bots.** {e}")
        logging.exception(e)
