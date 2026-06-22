from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

def register(app):

    @app.on_message(filters.command("start"))
    async def start_cmd(client, message):

        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ أضف البوت لمجموعتك",
                        url="https://t.me/YOUR_BOT_USERNAME?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📢 القناة",
                        url="https://t.me/QQHMDQ"
                    ),
                    InlineKeyboardButton(
                        "👨‍💻 المطور",
                        url="https://t.me/Q_0_R"
                    )
                ]
            ]
        )

        await message.reply_photo(
            photo="https://picsum.photos/800/400",
            caption="""
🎵 مرحباً بك في سورس سوريا ميوزك

• تشغيل الأغاني
• تشغيل الفيديو
• قوائم تشغيل
• تحكم كامل بالمحادثة الصوتية
            """,
            reply_markup=buttons
        )
