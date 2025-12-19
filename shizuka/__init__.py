import os
import asyncio
import threading

# Python 3.12+ compatibility fix
try:
    asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

from pyrogram import Client

API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
TOKEN = os.environ.get("TOKEN", None)
START_IMG = os.environ.get(
    "START_IMG",
    "https://files.catbox.moe/s0gtn8.jpg",
)

SHIZUKA = Client(":memory:", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
