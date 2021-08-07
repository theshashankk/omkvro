from telethon import events
from telethon import Button
from .. import xd, OWNER_ID

@xd.on(events.NewMessage(incoming=True, pattern="/start"))
async def strat(e):
  but = [[Button.url('Creator 💜', "t.me/Albertt_xD")]]
  but += [[Button.inline('Utils', data="utttils")]]
  but += [[Button.url('Gay', f"tg://user?id={e.sender.id}")]]
  await xd.send_file(e.chat_id, file="CAADBQADAgMAAlLIEVTp_wdXuvZM8QI")
  await e.reply(e.chat_id, buttons=but)
