from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

def register(app):

    @app.on_message(filters.regex("^تشغيل (.+)"))
    async def play(_, message):

        query = message.text.split(" ", 1)[1]

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
            photo="https://picsum.photos/800/450",
            caption=f"""
🎵 جاري التشغيل

🎧 الأغنية:
{query}

👤 بواسطة:
{message.from_user.mention}

━━━━━━━━━━
⏳ المدة: غير معروفة
            """,
            reply_markup=buttons
        )

    @app.on_message(filters.regex("^فيديو (.+)"))
    async def vplay(_, message):

        query = message.text.split(" ", 1)[1]

        await message.reply(
            f"🎬 جاري تشغيل الفيديو:\n\n{query}"
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
