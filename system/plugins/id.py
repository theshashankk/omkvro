from telethon import events
from telethon.utils import pack_bot_file_id
from .. import xd

@xd.on(events.NewMessage(pattern="^/id"))
async def _(event):
    if event.reply_to_msg_id:
        await event.get_input_chat()
        omk = [[Button.inline('Close 🚧', data='omkcls')]]
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await xd.send_message(
                event.chat_id,
                f"Current Chat ID: `{event.chat_id}`\nFrom User ID: `{r_msg.from_id}`\nBot API File ID: `{bot_api_file_id}`",
                button=omk,
                 ),
            )
        else:
            await xd.send_message(
                event.chat_id,
                f"Current Chat ID: `{event.chat_id}`\nFrom User ID: `{r_msg.from_id}`",
                button=omk
                ),
            )
    else:
        await xd.send_message(
            event.chat_id, "Current Chat ID: `{}`".format(str(event.chat_id))
        )
