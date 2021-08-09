from . import *
from .. import xd
@xd.on(events.NewMessage(incoming=True, pattern="/gcast")
async def _(e):
    if str(e.sender_id) in all_sudo():
        msg = e.pattern_match.group(1)
        for x in all_chats():
            try:
                await bot.send_message(int(x), msg)
                await e.reply(f"🚧 Broadcast done in {len(x)} Chats")
            except Exception as err:
                await e.reply(f"🚧 Error {str(err)}")  
    else:
        await e.reply("**chla ja bsdk**")
