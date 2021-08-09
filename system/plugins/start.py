from telethon import Button, events

from .. import xd, OWNER_ID


@xd.on(events.NewMessage(incoming=True, pattern="/start"))
async def strat(e):
    but = [[Button.url("Creator 💜", "t.me/Albertt_xD")]]
    but += [[Button.inline("Utils", data="utttils")]]
    but += [[Button.url("Gay", f"tg://user?id={e.sender.id}")]]
    omk = [[Button.url("🐼 Creator 🐼", "t.me/Albertt_xD")]]
    if e.sender_id == OWNER_ID:
        return await e.reply(e.chat_id, "Hemlo sur", buttons=but)
    else:
        await e.reply("CONTACT MY OWNER TU ACCESS ME", button=omk)
    
    
"""
await xd.send_file(e.chat_id, file="CAADBQADAgMAAlLIEVTp_wdXuvZM8QI")

    await e.reply(e.chat_id, buttons=but)
"""
