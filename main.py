from pyrogram import Client
from config import *

app = Client(
    "SYRIA-MUSIC",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

from plugins.start import register as start_register
start_register(app)

from plugins.play import register as play_register
play_register(app)

from plugins.admins import register as admin_register
admin_register(app)

from plugins.callbacks import register as callbacks_register
callbacks_register(app)

print("SYRIA MUSIC STARTED")

app.run()
