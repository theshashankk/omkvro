from telethon import events
from .. import xd

@xd.on(events.NewMessage(incoming=True, pattern="/infoo"))
async def stick(event):
  lwda = await event.get_reply_message()
  await xd.reply(event.chat_id, f"Your sticker id: `{lwda.file.id}`")
