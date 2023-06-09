
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden

FSUB = "accdzuserbot"

@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not FSUB:  
        return
    try:
        try:
            await bot.get_chat_member(FSUB, msg.from_user.id)
        except UserNotParticipant:
            if FSUB.isalpha():
                link = "https://t.me/" + FSUB
            else:
                chat_info = await bot.get_chat(FSUB)
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"TEXT FSUB",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("ADMIN 👤", url="https://t.me/MSDZULQRNN")],
                        [InlineKeyboardButton("CHANNEL", url="https://t.me/MSPR0JECT"),
                         InlineKeyboardButton("SUPPORT", url="https://t.me/envSample")],
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Kamu bukan admin!")
