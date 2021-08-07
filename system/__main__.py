from sys import argv
from system.config import Config
from system import xd
from system import logging
from pathlib import Path
from sys import argv
import telethon.utils
from telethon import TelegramClient
from system.utils import xd_cmd, start_xd
import glob



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    xd.start(bot_token=Config.BOT_TOKEN)
    
path = "plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        start_chatbot(shortname.replace(".py", ""))

print("Your bot is alive")
print("f")
print("u")
print("c")
print("k")

if len(argv) not in (1, 3, 4):
    xd.disconnect()
else:
    xd.run_until_disconnected()
