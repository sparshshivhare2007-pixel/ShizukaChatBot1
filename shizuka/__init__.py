import os
import asyncio
from pyrogram import Client

# Python version compatibility fix
try:
    asyncio.get_event_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
TOKEN = os.environ.get("TOKEN", None)
START_IMG = os.environ.get(
    "START_IMG",
    "https://files.catbox.moe/s0gtn8.jpg",
)

# ":memory:" ki jagah "shizuka" use karein taaki time sync issue na aaye
SHIZUKA = Client(
    "shizuka",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TOKEN,
    workers=20
)
