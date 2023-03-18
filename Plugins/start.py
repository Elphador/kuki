from pyrogram import filters
from datetime import datetime
from  __init__ import *
import json

with open("extensions/reply/text.json","r",encoding="UTF-8") as data:
    text = json.load(data)

@bot.on_message(filters.private & filters.command("start"))
async def start(client, message):
    f_name = message.from_user.first_name 
    user_id = message.chat.id
    username = message.from_user.username  
    database.add_user(f_name,user_id,username,str(datetime.now)) if database.exist(user_id) else ""
    await client.send_message(user_id,text["start"].format(message.from_user.mention),reply_markup=start_btn) 
