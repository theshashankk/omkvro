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

@xd.on(events.callbackquery.CallbackQuery(data="uttils"))
async def ut(e):
    await e.edit(e.chat_id, "HERE IS MY UTILS MENU", button=[
             [
                 Button.inline("Add Keyboard", data="addk"),
                 Button.inline("Start Buttons", data="go")
             ],
             [
                 Button.inline("Remove Keyboard", data="removek"),
                 Button.inline("List Poles", data="listp")
             ],
             [
                 Button.inline("Add Sudo", data="adds"),
                 Button.inline("Remove Sudo", data="rems"),
                 Button.inline("List Sudo", data="lists")
             ],
             [
                Button.inline("Eval", data="eval"),
                Button.inline("Broadcast", data="bcast")
             ],
             [
                Button.inline("Translate", data="tr"),
                Button.inline("Get Id", data="id")
             ],
             [
                Button.inline("My Master", data="me")
             ],
             [
                Button.inline("Back", data="start")
             ],
         ]
