from pyrogram import filters

def register(app):

    @app.on_message(filters.regex("^تشغيل (.+)"))
    async def play(_, message):

        query = message.text.split(
            " ", 1
        )[1]

        await message.reply(
            f"🎵 جاري البحث عن:\n\n{query}"
        )

    @app.on_message(filters.regex("^فيديو (.+)"))
    async def vplay(_, message):

        query = message.text.split(
            " ", 1
        )[1]

        await message.reply(
            f"🎬 جاري البحث عن الفيديو:\n\n{query}"
        )

    @app.on_message(filters.regex("^قائمتي$"))
    async def mylist(_, message):

        await message.reply(
            "📜 قائمة التشغيل فارغة"
        )

    @app.on_message(filters.regex("^اضف_للقائمة (.+)"))
    async def add_playlist(_, message):

        song = message.text.split(
            " ", 1
        )[1]

        await message.reply(
            f"✅ تمت إضافة:\n{song}"
        )
