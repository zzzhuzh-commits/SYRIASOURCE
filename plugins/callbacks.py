from pyrogram import filters
from pyrogram.types import CallbackQuery
from config import OWNER_ID

def register(app):

    @app.on_callback_query(filters.regex("^skip$"))
    async def skip_cb(_, query: CallbackQuery):

        if query.from_user.id != OWNER_ID:
            return await query.answer(
                "هذا الزر للمطور فقط",
                show_alert=True
            )

        await query.message.reply("⏭ تم التخطي")
        await query.answer()

    @app.on_callback_query(filters.regex("^stop$"))
    async def stop_cb(_, query: CallbackQuery):

        if query.from_user.id != OWNER_ID:
            return await query.answer(
                "هذا الزر للمطور فقط",
                show_alert=True
            )

        await query.message.reply("⏹ تم الإيقاف")
        await query.answer()

    @app.on_callback_query(filters.regex("^resume$"))
    async def resume_cb(_, query: CallbackQuery):

        if query.from_user.id != OWNER_ID:
            return await query.answer(
                "هذا الزر للمطور فقط",
                show_alert=True
            )

        await query.message.reply("▶️ تم الاستئناف")
        await query.answer()
