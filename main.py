from pyrogram import Client

from config import *

app = Client(
    "HMD-ALSOURY-BEST",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

from plugins.start import register as start_register
start_register(app)

from plugins.play import register as play_register
play_register(app)

print("HMD-ALSOURY-BEST Started")

app.run()
