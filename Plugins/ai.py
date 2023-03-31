from pyrogram import Client as bot
from pyrogram import filters
from pyrogram.errors import *
from __init__ import database
import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-M135FU) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36',
    'Referer': 'https://chat.kuki.ai/chat',
}

@bot.on_message(filters.private & filters.text)
async def main(client,message):
    data = {
    'uid': '5e75deba0d058047',
    'input': msg.text,
    'sessionid': '483732535',
    }
    await message.reply(message.text)
    resp = requests.post('https://icap.iconiq.ai/talk', headers=headers, data=data)
    json_resp = json.loads(resp.text)
    decoded_resp = json_resp['responses'][0]

    intial = 0 

    for i in range(int(len(decoded_resp)/4000)+1):
        old_intial = intial
        intial += 4000
        print(decoded_resp)
        await message.reply(decoded_resp[old_intial:intial])
