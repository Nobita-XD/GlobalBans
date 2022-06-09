import importlib
import asyncio
from contextlib import closing, suppress
from pyrogram import idle
from uvloop import install
from Abhi import GBAN_LOG_GROUP_ID, app, log
from Abhi.Plugins import ALL_MODULES
from Abhi.Utils.restart import clean_restart_stage

loop = asyncio.get_event_loop()

async def init():
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Abhi.Plugins" + all_module)
    log("Abhi.Plugins").info(
        "Successfully Imported Modules "
    )
    
if __name__ == "__main__":
    loop.run_until_complete(init())
    log("Abhi").info("Stopping Gban Bot! GoodBye")
    
