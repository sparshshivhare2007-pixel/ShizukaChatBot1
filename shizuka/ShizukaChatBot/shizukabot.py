import asyncio
import re
import aiohttp
import emoji
import requests
from gpytranslate import Translator
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from shizuka import SHIZUKA

url = "https://acobot-brainshop-ai-v1.p.rapidapi.com/get"
translator = Translator()
BOT_ID = 1699240021

def extract_emojis(s):
    # Fixed for emoji 2.0+
    return "".join(c for c in s if c in emoji.EMOJI_DATA)

en_chats = []

@SHIZUKA.on_message(
    filters.text & filters.reply & ~filters.bot & ~filters.via_bot & ~filters.forwarded,
    group=2,
)
async def lycia(client, message):
    if message.reply_to_message.from_user.id != BOT_ID:
        message.continue_propagation()
    
    msg = message.text
    chat_id = message.chat.id
    hello = message.from_user.id
    
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
        
    if chat_id in en_chats:
        onik = msg
        querystring = {
            "bid": "161901",
            "key": "Sgv5QAk5wEbhqYn0",
            "uid": str(hello),
            "msg": onik,
        }
        headers = {
            "X-RapidAPI-Host": "acobot-brainshop-ai-v1.p.rapidapi.com",
            "X-RapidAPI-Key": "a1fa7cb243msh40ac83d27b168ddp1fdc80jsn7d0db8bffc62",
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        result = response.json().get("cnt", "I'm not sure what to say.")
        
        try:
            await SHIZUKA.send_chat_action(message.chat.id, "typing")
            await message.reply_text(result)
        except Exception as e:
            print(e)
    else:
        u = msg.split()
        emj = extract_emojis(msg)
        rm = msg.replace(emj, "")
        
        # Simple cleanup for mentions/hashtags
        rm = " ".join(filter(lambda x: not x.startswith(("@", "#", "/")), u))
        
        detection = await translator.detect(rm)
        lan = detection if isinstance(detection, str) else detection.lang
        
        onik = rm
        if lan != "en":
            tr_res = await translator.translate(onik, targetlang="en")
            onik = tr_res.text

        querystring = {
            "bid": "161901",
            "key": "Sgv5QAk5wEbhqYn0",
            "uid": str(hello),
            "msg": onik,
        }
        headers = {
            "X-RapidAPI-Host": "acobot-brainshop-ai-v1.p.rapidapi.com",
            "X-RapidAPI-Key": "a1fa7cb243msh40ac83d27b168ddp1fdc80jsn7d0db8bffc62",
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        saini = response.json().get("cnt", "Error connecting to brain.")

        if lan != "en":
            tr_back = await translator.translate(saini, targetlang=lan)
            saini = tr_back.text

        try:
            await SHIZUKA.send_chat_action(message.chat.id, "typing")
            await message.reply_text(saini)
        except Exception as e:
            print(e)

@SHIZUKA.on_message(filters.text & filters.private & ~filters.bot)
async def chankit(client, message):
    msg = message.text
    hello = message.from_user.id
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    
    u = msg.split()
    emj = extract_emojis(msg)
    rm = msg.replace(emj, "")
    rm = " ".join(filter(lambda x: not x.startswith(("@", "#", "/")), u))
    
    detection = await translator.detect(rm)
    lan = detection if isinstance(detection, str) else detection.lang
    
    onik = rm
    if lan != "en":
        tr_res = await translator.translate(onik, targetlang="en")
        onik = tr_res.text

    querystring = {
        "bid": "161901",
        "key": "Sgv5QAk5wEbhqYn0",
        "uid": str(hello),
        "msg": onik,
    }
    headers = {
        "X-RapidAPI-Host": "acobot-brainshop-ai-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "a1fa7cb243msh40ac83d27b168ddp1fdc80jsn7d0db8bffc62",
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    saini = response.json().get("cnt", "...")

    if lan != "en":
        tr_back = await translator.translate(saini, targetlang=lan)
        saini = tr_back.text

    try:
        await SHIZUKA.send_chat_action(message.chat.id, "typing")
        await message.reply_text(saini)
    except Exception as e:
        print(e)

@SHIZUKA.on_message(
    filters.regex("(?i)(Lycia|SHIZUKA|shizuka)")
    & ~filters.bot
    & ~filters.via_bot
    & ~filters.forwarded
    & ~filters.reply
    & ~filters.channel,
)
async def chankitsaini(client, message):
    msg = message.text
    hello = message.from_user.id
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
        
    u = msg.split()
    rm = " ".join(filter(lambda x: not x.startswith(("@", "#", "/")), u))
    
    detection = await translator.detect(rm)
    lan = detection if isinstance(detection, str) else detection.lang
    
    onik = rm
    if lan != "en":
        tr_res = await translator.translate(onik, targetlang="en")
        onik = tr_res.text

    querystring = {
        "bid": "161901",
        "key": "Sgv5QAk5wEbhqYn0",
        "uid": str(hello),
        "msg": onik,
    }
    headers = {
        "X-RapidAPI-Host": "acobot-brainshop-ai-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "a1fa7cb243msh40ac83d27b168ddp1fdc80jsn7d0db8bffc62",
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    saini = response.json().get("cnt", "Yes?")

    if lan != "en":
        tr_back = await translator.translate(saini, targetlang=lan)
        saini = tr_back.text

    try:
        await SHIZUKA.send_chat_action(message.chat.id, "typing")
        await message.reply_text(saini)
    except Exception as e:
        print(e)
