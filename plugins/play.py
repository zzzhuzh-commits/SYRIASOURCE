from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

def register(app):

    @app.on_message(filters.text)
    async def play_handler(client, message):

        if not message.text:
            return

        if message.text.startswith("تشغيل "):

            song = message.text.replace(
                "تشغيل ",
                "",
                1
            )

            buttons = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "⏭ تخطي",
                            callback_data="skip"
                        ),
                        InlineKeyboardButton(
                            "⏸ ايقاف",
                            callback_data="pause"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "▶️ استئناف",
                            callback_data="resume"
                        ),
                        InlineKeyboardButton(
                            "❌ اغلاق",
                            callback_data="close"
                        )
                    ]
                ]
            )

            await message.reply_photo(
                photo="https://picsum.photos/700/400",
                caption=f"""
🎵 جاري التشغيل...

🎧 الأغنية:
{song}

👤 بواسطة:
{message.from_user.mention}
                """,
                reply_markup=buttons
            )
