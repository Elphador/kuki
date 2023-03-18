from extensions.filter.channel_filter import *
from pyrogram import filters
from __init__ import *
import json

with open("extensions/reply/text.json","r",encoding="UTF-8") as data:
    text = json.load(data)

@bot.on_message(channel_filter & filters.private)
async def c_force(client,message):
    await message.reply(text["force_text"],reply_markup=channel_btn)
