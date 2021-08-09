import os


class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    REDIS_URI = os.environ.get("DATABASE_URL", None)
    API_HASH = os.environ.get("API_HASH", None)
    APP_ID = int(os.environ.get("APP_ID", 6))
    OWNER_ID = int(os.environ.get("OWNER_ID", None))
    COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", "^/")
    DUMB_CHAT = int(os.environ.get("DUMB_CHAT", False))
    CUSTOM_START = os.environ.get("CUSTOM_START", None)
    JMT_ENABLE = os.environ.get("JMT_ENABLE", False)
    JMTC_ID = int(os.environ.get("JMTC_ID", False))
    JMTC_LINK = os.environ.get("JMTC_LINK", "t.me/AboutShashankxD")
    CUSTOM_IMG = os.environ.get(
        "CUSTOM_IMG",
        "https://static.botsrv.com/website/img/quriobot_favicon.1727b193.png",
    )
    REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", None)
