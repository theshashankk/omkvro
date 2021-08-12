from telethon import events

from system.BotConfig import Config

from .. import xd

# \\
SMEX_ID = Config.OWNER_ID
text = []
# //
@xd.on(events.NewMessage(incoming=True, pattern="/add"))
async def add(event):
    if not event.is_group:
        return
    if event.sender_id == SMEX_ID:
        try:
            lwda = event.pattern_match.group(1)
            text.append(lwda)
            await event.reply(event.chat_id, f"__Done__ Added\n**{lwda}**")
        except Exception as x:
            await event.reply(f"Error {str(x)}")
    else:
        await event.reply(event.chat_id, "__JANA XHKKE__")


@xd.on(events.NewMessage(incoming=True, pattern="/smwx"))
async def main(event):
    lel = event.pattern_match.group(1)
    [[Button.text(f"{lel}")]]
    await xd.send_file(
        event.chat_id,
        file="CAACAgUAAxkBAAELN8hhESppbDCjneoJnOfCZMpTHnayFQAClwIAAver2FTTWdasUnQxayAE",
        buttons=omk,
    )
