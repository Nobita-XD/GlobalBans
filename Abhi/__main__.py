import importlib
import asyncio
from contextlib import closing, suppress
from pyrogram import idle
from uvloop import install
from Abhi import GBAN_LOG_GROUP_ID, app, log
from Abhi.Plugins import ALL_MODULES
from Abhi.Utils.restart import clean_restart_stage


async def start_bot():
    await app.start()
    log.info("[ INFO ] BOT & USERBOT CLIENT STARTED")
    
    await idle()
    log.info("[ INFO ] BOT & USERBOT CLIENT STOPPED")
    await app.stop()


event = asyncio.get_event_loop_policy()
event_loop = event.new_event_loop()
event_loop.run_until_complete(start_bot())        
