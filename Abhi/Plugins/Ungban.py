from pyrogram import filters 
from Abhi.Utils.errors import capture_err
from Abhi.Core.extract import extract_user
from Abhi.Database.Gbandb import is_gbanned_user, remove_gban_user



@app.on_message(filters.command("ungban") & SUDOERS & ~filters.edited)
@capture_err
async def unban_globally(_, message):
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply_text("I can't find that user.")
    user = await app.get_users(user_id)

    is_gbanned = await is_gbanned_user(user.id)
    if not is_gbanned:
        await message.reply_text("I don't remember Gbanning him.")
    else:
        await remove_gban_user(user.id)
        await message.reply_text(f"Lifted {user.mention}'s Global Ban.'")
