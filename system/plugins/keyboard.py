from telethon import events, Button
from .. import db, xd
from system.BotConfig import Config
# \\
SMEX_ID = Config.OWNER_ID
# //
@xd.on(events.NewMessage(incoming=True, pattern="/add"))
async def add(event):
    if event.sender_id == SMEX_ID:
        try:
            lwda = event.pattern_match.group(1)
            text.append(lwda)
            await event.reply(event.chat_id, f"__Done__ Added\n**{lwda}**")
        except Exception as x:
            await event.reply(f"Error {str(x)}")
    else:
        await event.reply(event.chat_id, "__JANA XHKKE__")