from pyrogram import Client as bot
from pyrogram import filters
from extensions.database.database import database
import json


with open("extensions/reply/text.json","r",encoding="UTF-8") as data:
    text = json.load(data)

@bot.on_message(filters.private & filters.command("feedback"))
async def feedback(client,message):
    user_id = message.chat.id 
    feedback = message.text.replace('/feedback','')
    for admin in database.get_admin():
        await client.send_message(admin,f"Feedback from {user_id}\n{feedback}")   
    
@bot.on_message( filters.private & filters.command("users")) 
async def users(client, message):
    users = database.users_num()
    await message.reply(text["status"].format(users))
@bot.on_message(filters.command("usernames")) 
async def each_users(client,message):
    users = database.get_users()
    names = ""
    for usr in users:
        names+=f"{usr['name']} => @{usr['username']} => Joined in {usr['date']}\n"
await message.reply(names)
