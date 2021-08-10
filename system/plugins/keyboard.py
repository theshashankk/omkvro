from telethon import events, Button
from .. import db, xd
#\\
@xD.on(events.NewMessage(incoming=True, pattern="/add"))
async def lwda(event):
  if event.sender_id == SMEX_ID:
    try:
      lwda = event.pattern_match.group(1)
      text.append(lwda)
      await event.reply(event.chat_id, "Done added\nWanna Add more 🤔🤔\nType /add <txt>")
  else:
    await event.reply(event.chat_id, "JANA LWDE")
