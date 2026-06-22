from pyrogram import filters

def register(app):

    @app.on_message(filters.command("تشغيل"))
    async def play(_, message):
        if len(message.command) < 2:
            return await message.reply("اكتب:\nتشغيل اسم الأغنية")

        query = " ".join(message.command[1:])

        await message.reply(
            f"🎵 جاري البحث عن:\n{query}"
        )

    @app.on_message(filters.command("فيديو"))
    async def video(_, message):
        if len(message.command) < 2:
            return await message.reply("اكتب:\nفيديو اسم الفيديو")

        query = " ".join(message.command[1:])

        await message.reply(
            f"🎬 جاري البحث عن الفيديو:\n{query}"
        )
