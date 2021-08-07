# // @Albertt_xD \\
# \\ @Albertt_xD //
import sys
import logging
from telethon import events
import functools
import glob
import inspect
import importlib
from pathlib import Path
from system.config import Config
from . import xd

bothandler = Config.COMD_HNDLR
def xd_cmd(add_cmd, is_args=False):
    def cmd(func):
        if is_args:
            pattern = bothandler + add_cmd + "(?: |$)(.*)"
        else:
            pattern = bothandler + add_cmd + "$"
        xd.add_event_handler(
            func, events.NewMessage(incoming=True, pattern=pattern)
        )

    return cmd

def shashank_only():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            moms = Config.OWNER_ID
            if event.sender_id == moms:
                await func(event)
            else:
                pass

        return wrapper

    return decorator
  
def load_plugins(plugin_name):
    path = Path(f"plugins/{plugin_name}.py")
    name = "plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["plugins." + plugin_name
