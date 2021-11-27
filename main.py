from telethon import events, TelegramClient

import re, os, random, asyncio, logging, html

logging.basicConfig(

    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO

)

LOGGER = logging.getLogger(name)

APP_ID = os.environ.get("18622297")

API_HASH = os.environ.get("27e6993af0786f66f96599db6cd10bcc")

BOT_TOKEN = os.environ.get("2124077071:AAHubMO4S7WZUhSNMbYA6Ix4fsp3GfuoNcY")

bot = TelegramClient("bot", APP_ID, API_HASH).start(bot_token=BOT_TOKEN)

print("Bot started")

bot.run_until_disconnected()
