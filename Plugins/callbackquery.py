from pyrogram import Client as bot
import json

with open("extensions/reply/text.json","r",encoding="UTF-8") as data:
    text = json.load(data)


@bot.on_callback_query() 
async def query(client,callbackquery):
    name = callbackquery.message.from_user.first_name
    user_id = callbackquery.message.chat.id
    data = callbackquery.data
    if data == "help":
        await callbackquery.message.reply(text["help"])
    else:
        await callbackquery.message.reply(text["Error_1"])