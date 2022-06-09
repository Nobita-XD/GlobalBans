import importlib
import asyncio
from contextlib import closing, suppress
from pyrogram import idle
from uvloop import install
from Abhi import GBAN_LOG_GROUP_ID, app, log
from Abhi.Plugins import ALL_MODULES
from Abhi.Utils.restart import clean_restart_stage

loop = asyncio.get_event_loop()

HELPABLE = {}


async def start_bot():
    global HELPABLE

    for module in ALL_MODULES:
        imported_module = importlib.import_module("Abhi.Plugins." + module)
        if (
                hasattr(imported_module, "__MODULE__")
                and imported_module.__MODULE__
        ):
            imported_module.__MODULE__ = imported_module.__MODULE__
            if (
                    hasattr(imported_module, "__HELP__")
                    and imported_module.__HELP__
            ):
                HELPABLE[
                    imported_module.__MODULE__.replace(" ", "_").lower()
                ] = imported_module
    bot_modules = ""
    j = 1
    for i in ALL_MODULES:
        if j == 4:
            bot_modules += "|{:<15}|\n".format(i)
            j = 0
        else:
            bot_modules += "|{:<15}".format(i)
        j += 1
    print("+===============================================================+")
    print("|                          GLOBAL BANS                              |")
    print("+===============+===============+===============+===============+")
    print(bot_modules)
    print("+===============+===============+===============+===============+")
    log.info(f"BOT STARTED AS NobitaXD Gban Code!")
    

    
