from Abhi import app, OWNER_ID, GBAN_LOG_GROUP_ID
from pyrogram import filters
from Abhi.Core.extract import extract
from Abhi.Database.Gbandb import add_gban_user
from Abhi.Database.chats import get_served_chats
from Abhi.Utils.errors import capture_err


@app.on_message(filters.command("gban") & filters.user(OWNER_ID) & ~filters.edited)
@capture_err
async def ban_globally(_, message):
    user_id, reason = await extract(message)
    user = await app.get_users(user_id)
    from_user = message.from_user

    if not user_id:
        return await message.reply_text("I can't find that user.")
    if not reason:
        return await message.reply("No reason provided.")

    
    served_chats = await get_served_chats()
    m = await message.reply_text(
        f"**Banning {user.mention} Globally!**"
        + f" **This Action Should Take About {len(served_chats)} Seconds.**"
    )
    await add_gban_user(user_id)
    number_of_chats = 0
    for served_chat in served_chats:
        try:
            await app.ban_chat_member(served_chat["chat_id"], user.id)
            number_of_chats += 1
            await asyncio.sleep(1)
        except FloodWait as e:
            await asyncio.sleep(int(e.x))
        except Exception:
            pass
    try:
        await app.send_message(
            user.id,
            f"Hello, You have been globally banned by {from_user.mention},"
            + " You can appeal for this ban by talking to him.",
        )
    except Exception:
        pass
    await m.edit(f"Banned {user.mention} Globally!")
    ban_text = f"""
__**New Global Ban**__
**Origin:** {message.chat.title} [`{message.chat.id}`]
**Admin:** {from_user.mention}
**Banned User:** {user.mention}
**Banned User ID:** `{user_id}`
**Reason:** __{reason}__
**Chats:** `{number_of_chats}`"""
    try:
        m2 = await app.send_message(
            GBAN_LOG_GROUP_ID,
            text=ban_text,
            disable_web_page_preview=True,
        )
        await m.edit(
            f"Banned {user.mention} Globally!\nAction Log: {m2.link}",
            disable_web_page_preview=True,
        )
    except Exception:
        await message.reply_text(
            "User Gbanned, But This Gban Action Wasn't Logged, Add Me Bot In GBAN_LOG_GROUP"
        )
