from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from core.youtube import search_youtube

def register(app):

    @app.on_message(filters.text)
    async def play_handler(client, message):

        if not message.text:
            return

        if not message.text.startswith("تشغيل "):
            return

        query = message.text.replace(
            "تشغيل ",
            "",
            1
        )

        msg = await message.reply_text(
            "🔎 جاري البحث..."
        )

        result = await search_youtube(query)

        if not result:
            return await msg.edit_text(
                "❌ لم يتم العثور على نتائج."
            )

        duration = result["duration"]

        minutes = duration // 60
        seconds = duration % 60

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
            photo=result["thumbnail"],
            caption=f"""
🎵 جاري التشغيل ...

🎧 الأغنية:
{result['title']}

⏱ المدة:
{minutes}:{seconds:02}

👤 بواسطة:
{message.from_user.mention}
            """,
            reply_markup=buttons
        )

        await msg.delete()
