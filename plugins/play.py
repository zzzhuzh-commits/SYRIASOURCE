from pyrogram import filters

def register(app):

    @app.on_message(filters.text)
    async def play_cmd(client, message):

        if not message.text:
            return

        if message.text.startswith("تشغيل "):

            song = message.text.replace("تشغيل ", "", 1)

            await message.reply_text(
                f"🎵 جاري البحث عن:\n\n{song}"
            )
