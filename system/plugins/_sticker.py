from telethon import events
from .. import xd

@xd.on(events.NewMessage(incoming=True, pattern="/infoo"))
async def stick(event):
  lwda = await event.get_reply_message()
  await xd.send_message(event.chat_id, f"Your sticker id: `{lwda.file.id}`")
