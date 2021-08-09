import glob
import logging
from pathlib import Path

from system.utils import load_plugins

from . import xd

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)

path = "system/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

sm3x = """
░█▀▀▀█ ░█▀▄▀█ ░█▀▀▀ ▀▄░▄▀ 
─▀▀▀▄▄ ░█░█░█ ░█▀▀▀ ─░█── 
░█▄▄▄█ ░█──░█ ░█▄▄▄ ▄▀░▀▄"""
print(sm3x)
print("smex")
print("smex")
print("smex")
print("smex")
print("smex")

if __name__ == "__main__":
    xd.run_until_disconnected()
