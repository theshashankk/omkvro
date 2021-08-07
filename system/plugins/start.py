from telethon import events
from telethon import Button
from .. import xd, OWNER_ID

@xd.on(events.NewMessage(incoming=True, pattern="/start"))
async def strat(e):
  but = [[Button.url('Creator 💜', "t.me/Albertt_xD")]]
  but += [[Button.inline('Utils', data="utttils")]]
  but += [[Button.url('Gay', f"tg://user?id={e.sender.id}")]]
  if e.sender_id not in OWNER_ID:
    return await xd.send_file(e.chat_id, file="link")
  await xd.send_message(e.chat_id, button=but)
  if e.sender_id == OWNER_ID:
    return await xd.send_message(e.chat_id, "HEMLO SUR")
