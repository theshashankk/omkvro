from telethon import Button, events

from system.BotConfig import Config

from .. import xd

# // SMEX \\
SMEX_ID = Config.OWNER_ID
# \\ SMEX //
@xd.on(events.NewMessage(incoming=True, pattern="/start"))
async def strat(e):
    but = [[Button.url("Creator 💜", "t.me/Albertt_xD")]]
    but += [[Button.inline("Utils", data="utis")]]
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
# Callback
@xd.on(events.callbackquery.CallbackQuery(data="cls"))
async def omk(e):
    await e.delete()


@xd.on(events.callbackquery.CallbackQuery(data="utis"))
async def ut(e):
    sed = [[Button.inline("🐼 Comming soon", data="soon")]]
    await e.edit(e.chat_id, "HERE IS MY UTILS MENU", buttons=sed)
