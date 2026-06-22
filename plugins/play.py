from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from core.youtube import search_youtube

def register(app):

    @app.on_message(filters.regex("^تشغيل (.+)"))
    async def play(_, message):

        query = message.text.split(" ", 1)[1]

        result = search_youtube(query)

        if not result:
            return await message.reply(
                "❌ لم يتم العثور على نتائج"
            )

        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⏭ تخطي",
                        callback_data="skip"
                    ),
                    InlineKeyboardButton(
                        "⏹ إيقاف",
                        callback_data="stop"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "▶️ استئناف",
                        callback_data="resume"
                    ),
                    InlineKeyboardButton(
                        "❌ إغلاق",
                        callback_data="close"
                    )
                ]
            ]
        )

        await message.reply_photo(
            photo=result["thumbnail"],
            caption=f"""
🎵 جاري التشغيل

🏷 الاسم:
{result['title']}

⏱ المدة:
{result['duration']}

👤 بواسطة:
{message.from_user.mention}
            """,
            reply_markup=buttons
        )

    @app.on_message(filters.regex("^فيديو (.+)"))
    async def vplay(_, message):

        query = message.text.split(" ", 1)[1]

        result = search_youtube(query)

        if not result:
            return await message.reply(
                "❌ لم يتم العثور على نتائج"
            )

        await message.reply_photo(
            photo=result["thumbnail"],
            caption=f"""
🎬 الفيديو

🏷 الاسم:
{result['title']}

⏱ المدة:
{result['duration']}
            """
        )

    @app.on_message(filters.regex("^قائمتي$"))
    async def mylist(_, message):

        await message.reply(
            "📜 قائمة التشغيل فارغة"
        )

    @app.on_message(filters.regex("^اضف_للقائمة (.+)"))
    async def add_playlist(_, message):

        song = message.text.split(" ", 1)[1]

        await message.reply(
            f"✅ تمت إضافة:\n{song}"
        )
