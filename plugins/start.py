from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def register(app):

    @app.on_message(filters.command("start"))
    async def start(_, message):

        text = f"""
🎵 مرحباً بك في بوت الميوزك

• تشغيل : تشغيل أغنية
• فيديو : تشغيل فيديو
• قائمتي : عرض قائمتك
• اضف_للقائمة : حفظ أغنية

━━━━━━━━━━
👑 المطور يتحكم بالأوامر الإدارية
"""

        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ أضف البوت لمجموعتك",
                        url="https://t.me/YourBot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👨‍💻 المطور",
                        url="https://t.me/Q_0_R"
                    )
                ]
            ]
        )

        await message.reply_photo(
            photo="https://picsum.photos/800/500",
            caption=text,
            reply_markup=keyboard
        )
