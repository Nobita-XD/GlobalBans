from Abhi.Database import db
from typing import Dict, List, Union



chatsdb = db.chats

async def get_served_chats() -> list:
    chats_list = []
    async for chat in chatsdb.find({"chat_id": {"$lt": 0}}):
        chats_list.append(chat)
    return chats_list
