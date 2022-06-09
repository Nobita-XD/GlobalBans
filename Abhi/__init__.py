from os import environ
from pyrogram import Client





BOT_TOKEN = environ.get("BOT_TOKEN", None)
API_ID = int(environ.get("API_ID", 6))
API_HASH = environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
OWNER_ID = [int(x) for x in environ.get("OWNER_ID", "").split()]
MONGO_URL = environ.get("MONGO_URL", None)
GBAN_LOG_GROUP_ID = int(environ.get("LOG_GROUP_ID", None))

app = Client("Global Bans", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)
