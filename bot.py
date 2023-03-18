from pyrogram import Client as app
from config import *
proxy = {
     "scheme":"socks5",
     "hostname": "146.59.152.52",
     "port": 59166,
}
main_bot = app(
name="a",
proxy=proxy,
ipv6=True,
bot_token=bot_token
,api_id=api_id
,api_hash=api_hash,
plugins={"root":"Plugins","include":["start","channel_force","callbackquery","extra","admin","main"]})

main_bot.run()