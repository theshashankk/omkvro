import re, os, asyncio, html, logging
from telethon import TelegramClient, events, Button, functions
from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import pack_bot_file_id as lolpic


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.INFO)

try:
  BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
  APP_ID = int(os.environ.get("APP_ID", 6))
  API_HASH = os.environ.get("API_HASH", None)
  OWNER_ID = int(os.environ.get("OWNER_ID", None))
  
  
  
  print('Processing....')
except Exception as e:
  print(f"ERROR\n{str(e)}")


lol = TelegramClient('lol', APP_ID, API_HASH).start(bot_token=BOT_TOKEN)


async def check(ch, event, xD):
    try:
            sed = await xD(functions.channels.GetParticipantRequest(channel=ch, user_id=event.sender_id))
            if sed.participant:
                return True
    except telethon.errors.rpcerrorlist.UserNotParticipantError:
        return False

#Bhaag
      
@lol.on(events.NewMessage(pattern="[/!?=$-~.|}](start|START|Start)$"))
async def startkaru(event):
  but = [[Button.url('Creator 💜', "t.me/Albertt_xD")]]
  but += [[Button.inline('Utils', data="utttils")]]
  but += [[Button.url('Gay', f"tg://user?id={event.sender.id}")]]
  if event.is_private:
    return await event.reply(f'**Hey** [{event.sender.first_name}](tg://user?id={event.sender.id})!\n**Btw I only Work for @Albertt_xD 💜**', buttons=but)
  if event.sender_id in OWNER_ID:
    await event.reply(f"**Hey Master How are you 😉😉**")
  else:
    await shashank.reply("**Hemlo gay**")
    
@lol.on(events.callbackquery.CallbackQuery(data="utttils"))
async def umtils(event):
  but = [[Button.inline('🌚 Ping', data="pkng")]]
  but += [[Button.inline('🔰 filter', data="fiml")]]
  but += [[Button.inline('🔰 Memify', data="mememememem")]]
  but += [[Button.inline('🚧 Close', data="cls")]]
  await event.edit("**Here is utils menu**", button=but)
  
@lol.on(events.callbackquery.CallbackQuery(data="cls"))
async def cla(event):
  await event.delete()
    
print("Smex Bot Is Alive")
lol.run_until_disconnected()
