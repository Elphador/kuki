from __init__ import *
from pyrogram import filters
from pyrogram.errors import *
from time import sleep
import json
import asyncio


with open("extensions/reply/text.json","r",encoding="UTF-8") as data:
    text = json.load(data)

@bot.on_message(filters.private & filters.command("cast"))
async def cast(client,message):
    user_id = message.chat.id
    if  user_id in database.get_admin():
        txt = message.text
        block = " ."
        idinvalid  = " ."
        dec = " ."
        mesg = txt.replace('/cast',"")
        for user in database.get_user():
            try :
                await client.send_message(user['user_id'],mesg , reply_markup=mark)
            except UserIsBlocked:
                block += f"{user['user_id']} : {user['name']} :  @{user['username']}\n"
            except InputUserDeactivated:
                dec += f"{user['user_id']} : {user['name']} : @{user['username']}"
            except PeerIdInvalid:
                idinvalid += f" {user['user_id']} : {user['name']} : @{user['username']}"
            except FloodWait:
                await asyncio.sleep(30)     
            except Exception as error:
              await message.reply(error)
        await message.reply(f"cast logs\n\nBlocked User \n{block} \n Invalid Ids \n {idinvalid} Deactivated\n {dec}")

@bot.on_message(filters.command("msg"))  
async def admin_msg(client,message):
    user_id = message.chat.id
    if user_id in database.get_admin() :
        try :
            text = message.copy(message.text)
            ruid = text.split(" ")[1]
            mesgt = text.replace('/msg',"").replace(ruid,'')
            await bot.send_message(int(ruid), f"{mesgt}\n\n\n **Neural Programmers CEO**",reply_markup=mark) 
            await message.reply(text["sucess_admin"])
        except Exception as error:
            await message.reply(f"Not sent\n{error} ") 
        
@bot.on_message(filters.command("admins"))
async def add_admin(client,message):
    user_id = message.chat.id
    if user_id in database.get_admin():    
        result = " ."
        for admin in database.admins():
            admin_id = admin['admin']
            promoter_name = admin['promoted']
            result += f"id {admin_id} : promoted by {promoter_name} \n"
        await message.reply(result)

@bot.on_message(filters.command("force"))       
async def force(client,message):
    user_id = message.chat.id
    if user_id in database.get_admin():
        o_status = database.get_force_status()
        main_msg = await message.reply(f"**Current Force Join Status {o_status}🦊**")
        n_status = message.text.split(" ")[1]
        database.set_force_status(n_status)
        await asyncio.sleep(30)
        await main_msg.edit(f"**Current Force Join Set to {n_status}🦊**")

@bot.on_message(filters.private & filters.command("set"))
async def set(client, message):
    admin_id = message.text.replace("/set","")
    promoter = message.from_user.first_name 
    database.add_admin(admin_id,promoter)
    await client.send_message(int(admin_id),f"You have promoted to admin by {promoter}")
    await message.reply("Promoting New Admin Done🦊")
