from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def register(app):

    @app.on_message(filters.command("start"))
    async def start_cmd(client, message):

        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ اضف البوت للمجموعة",
                        url=f"https://t.me/{(await client.get_me()).username}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🎵 الاوامر",
                        callback_data="help"
                    )
                ]
            ]
        )

        await message.reply_text(
            """
🎵 اهلاً بك في HMD-ALSOURY-BEST

بوت ميوزك عربي متكامل

• تشغيل
• فيديو
• قوائم تشغيل
• اذاعات

اضغط الازرار بالاسفل
""",
            reply_markup=buttons
        )
