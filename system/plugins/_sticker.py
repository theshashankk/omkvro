from telethon import events, Button
from .. import xd

@xd.on(events.NewMessage(incoming=True, pattern="/infoo"))
async def stick(event):
  lwda = await event.get_reply_message()
  omk = [[Button.inline('🚧Close', data='omkcls')]]
  await event.reply(event.chat_id, f"🚧 Your sticker id: `{lwda.file.id}`", buttons=omk)

@xd.on(events.callbackquery.CallbackQuery(data="omkcls"))
async def even(event):
  await event.delete()
