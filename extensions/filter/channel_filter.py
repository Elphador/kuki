from pyrogram import filters
from __init__ import *
from config import *

def channel_filter(_,__,message):
    try:
        if database.get_force_status() == "on":
            user_id = message.chat.id
            all_users = []
            for i in __.get_chat_members(channel_id):
                all_users.append(i.user.id)
            if user_id not in all_users:
                return True
            else:
                return False
        else:
            return False
    except Exception:
        pass
channel_filter = filters.create(channel_filter)