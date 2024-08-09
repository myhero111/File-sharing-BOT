from pyrogram import Client, filters


API_ID = ""
API_HASH = ""
BOT_TOKEN = ""

Animefox = Client(
    name="fileshrebot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


print("Bot was STARTED")

Animefox.run()
