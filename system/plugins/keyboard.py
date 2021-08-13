from telethon import Button, events

from system.BotConfig import Config

from .. import xd

# \\
SMEX_ID = Config.OWNER_ID
text = []
# //
@xd.on(events.NewMessage(incoming=True, pattern="/add"))
async def add(e):
    if not e.is_group:
        return
    if e.sender_id == SMEX_ID:
        try:
            lwda = e.pattern_match.group(1)
            text.append(lwda)
            await e.reply(f"__Done__\n**Added: {lwda}")
        except Exception as x:
            await e.reply(f"🚧 Error {str(x)}")
    else:
        await e.reply("__JANA CHKKE__")


@xd.on(events.NewMessage(incoming=True, pattern="/smwx"))
async def main(event):
    lel = event.pattern_match.group(1)
    omk = [[Button.text(f"{lel}")]]
    if event.sender_id == SMEX_ID:
        return await xd.send_file(
            event.chat_id,
            file="CAACAgUAAxkBAAELN8hhESppbDCjneoJnOfCZMpTHnayFQAClwIAAver2FTTWdasUnQxayAE",
            buttons=omk,
        )
    else:
        await event.reply(event.chat_id, "__JANA BSDK__")
