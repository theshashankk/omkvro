from telethon import Button, events

from system.BotConfig import Config

from .. import xd

# // SMEX \\
SMEX_ID = Config.OWNER_ID
# \\ SMEX //
@xd.on(events.NewMessage(incoming=True, pattern="/start"))
async def strat(e):
    but = [[Button.url("Creator 💜", "t.me/Albertt_xD")]]
    but += [[Button.inline("Utils", data="utttils")]]
    but += [[Button.url("Gay", f"tg://user?id={e.sender.id}")]]
    omk = [
        [
            Button.url("🐼 Creator 🐼", "t.me/Albertt_xD"),
            Button.inline("🐼 Close 🐼", data="cls"),
        ]
    ]
    if e.sender_id == SMEX_ID:
        return await xd.send_message(e.chat_id, "Hemlo sur", buttons=but)
    else:
        await xd.send_message(e.chat_id, "CONTACT MY OWNER TU ACCESS ME", buttons=omk)


"""
a#wait xd.send_file(e.chat_id, file="CAADBQADAgMAAlLIEVTp_wdXuvZM8QI")

    await e.reply(e.chat_id, buttons=but)
"""
