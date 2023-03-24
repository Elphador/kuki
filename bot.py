from pyrogram import Client as app
from config import *

main_bot = app(
name="a",
bot_token=bot_token
,api_id=api_id
,api_hash=api_hash,
plugins={"root":"Plugins","include":["start","channel_force","callbackquery","extra","admin","ai"]})

main_bot.run()
