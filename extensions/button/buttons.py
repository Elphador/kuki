from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_btn = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Channel🌴",url='https://t.me/neuralp'),
            InlineKeyboardButton("Group🪺",url='https://t.me/neuralg')
        ],
        [
            InlineKeyboardButton("Subscribe Premium🍿",url='https://t.me/neuralf'),
            InlineKeyboardButton("Donate VPS🦭",url="https://t.me/neuralg")
        ],
        [
            InlineKeyboardButton("Help📃",callback_data='help')
        ]
    ]
)
channel_btn = InlineKeyboardMarkup([[InlineKeyboardButton("Join",url='https://t.me/neuralp')]])
mark = InlineKeyboardMarkup([[InlineKeyboardButton("🥬team Neural🌽",url = "https://t.me/neuralp")]])   