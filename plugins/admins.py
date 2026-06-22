from pyrogram import filters
from config import OWNER_ID

def register(app):

    @app.on_message(filters.command("اذاعة"))
    async def broadcast_cmd(client, message):

        if message.from_user.id != OWNER_ID:
            return

        await message.reply_text(
            "📢 سيتم إضافة نظام الإذاعة لاحقاً"
        )
