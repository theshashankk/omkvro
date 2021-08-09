# // @Albertt_xD \\
# \\ @Albertt_xD //
import importlib
import logging
import sys
from pathlib import Path


def load_plugins(plugin_name):
    path = Path(f"system/plugins/{plugin_name}.py")
    name = "system.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["system.plugins." + plugin_name] = load
    print("smex has Imported " + plugin_name)
