from pyrogram import filters
from config import OWNER_ID

def register(app):

    @app.on_message(filters.command("تخطي"))
    async def skip(_, message):

        if message.from_user.id != OWNER_ID:
            return await message.reply(
                "❌ هذا الأمر للمطور فقط"
            )

        await message.reply(
            "⏭ تم التخطي"
        )

    @app.on_message(filters.command("ايقاف"))
    async def stop(_, message):

        if message.from_user.id != OWNER_ID:
            return await message.reply(
                "❌ هذا الأمر للمطور فقط"
            )

        await message.reply(
            "⏹ تم الإيقاف"
        )

    @app.on_message(filters.command("استئناف"))
    async def resume(_, message):

        if message.from_user.id != OWNER_ID:
            return await message.reply(
                "❌ هذا الأمر للمطور فقط"
            )

        await message.reply(
            "▶️ تم الاستئناف"
        )

    @app.on_message(filters.command("اعادة_تشغيل"))
    async def restart(_, message):

        if message.from_user.id != OWNER_ID:
            return await message.reply(
                "❌ هذا الأمر للمطور فقط"
            )

        await message.reply(
            "🔄 تمت إعادة التشغيل"
        )
