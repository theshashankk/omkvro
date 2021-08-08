from system.plugins.sql.users_sql import add_me_in_db, his_userid
from system.plugins.sql.blacklist_sql import is_he_added
from telethon import custom, events, Button, functions
from .. import xd
import telethon
from telethon.tl.types import (
    Channel,
    Chat,
    User
)

from telethon.utils import pack_bot_file_id

@xd.on(events.NewMessage(func=lambda e: e.is_private))
async def all_messages_catcher(event):
    if is_he_added(event.sender_id):
        return
    if event.sender_id == Config.OWNER_ID:
        return
    if event.raw_text.startswith("/"):
        return
    if Config.JMT_ENABLE:
        try:
            result = await xd(
                functions.channels.GetParticipantRequest(
                    channel=Config.JMTC_ID, user_id=event.sender_id
                )
            )
        except telethon.errors.rpcerrorlist.UserNotParticipantError:
            await event.reply(f"**Hey If you want to talk to my master then first join the channel :)**",
                             buttons = [Button.url("Join Channel", Config.JMTC_LINK)])
            return
    await event.get_sender()
    sed = await event.forward_to(Config.OWNER_ID)
    add_me_in_db(sed.id, event.sender_id, event.id)
  
@xd.on(events.NewMessage(func=lambda e: e.is_private))
async def sed(event):
    msg = await event.get_reply_message()
    if msg is None:
        return
    real_nigga = msg.id
    msg_s = event.raw_text
    user_id, reply_message_id = his_userid(
        msg.id
        )
    if event.sender_id == Config.OWNER_ID:
        if event.raw_text.startswith("/"):
            return
        if event.text is not None and event.media:
            bot_api_file_id = pack_bot_file_id(event.media)
            await xd.send_file(user_id, file=bot_api_file_id, caption=event.text, reply_to=reply_message_id)
        else:
            msg_s = event.raw_text
            await xd.send_message(
            user_id,
            msg_s,
            reply_to=reply_message_id,
            )  
            
