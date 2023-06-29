from pyrogram import Client as app
from config import *

main_bot = app(
name="ak",
bot_token=bot_token
,api_id=api_id
,api_hash=api_hash,
plugins={"root":"Plugins"})

main_bot.run()
