from telethon import events

from .. import xd


@xd.on(events.NewMessage(incoming=True, pattern="/type"))
async def lol(event):
    lwda = event.pattern_match_group(1)
    if event.sender_id in SMEX_ID:
        await xd.send_message(event.chat_id, f"{lwda}")
    else:
        await event.reply(event.chat_id, "jana chkke")
