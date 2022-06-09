import importlib
import asyncio
from contextlib import closing, suppress
from pyrogram import idle
from uvloop import install
from Abhi import GBAN_LOG_GROUP_ID, app, log
from Abhi.Plugins import ALL_MODULES
from Abhi.Utils.restart import clean_restart_stage

log.info("Bot Started")
app.start()
