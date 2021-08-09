# \\ @Albertt_xD //
# // @Albertt_xD \\
import logging
import os
import time
from datetime import datetime
from logging import DEBUG, INFO, FileHandler, StreamHandler, basicConfig, getLogger

from decouple import config
from redis import ConnectionError, ResponseError, StrictRedis
from telethon import TelegramClient

from system.BotConfig import Config

LOGS = getLogger(__name__)

if os.path.exists("logs.txt"):
    os.remove("logs.txt")

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)
LOGS.info(
    """                    
█▀ ▀█▀ ▄▀█ █▀█ ▀█▀ █ █▄░█ █▀▀
▄█ ░█░ █▀█ █▀▄ ░█░ █ █░▀█ █▄█
    """
)

if not Config.APP_ID:
    LOGS.info("SED VAI PLEASE ADD API ID IN VARS")
    exit(1)

if not Config.API_HASH:
    LOGS.info("SEE VRO PLEASE ADD API HASH IN VARS")
    exit(1)

if not Config.BOT_TOKEN:
    LOGS.info("SED VRO PLEASE ADD BOT TOKEN")
    exit(1)

if not Config.REDIS_URI:
    LOGS.info("SED VRO PLEASE ADD REDIS URI IN VARS")
    exit(1)

if not Config.REDIS_PASSWORD:
    LOGS.info("SED VRO PLEASE ADD REDIS PASSWORD IN VARS")
    exit(1)

if not Config.OWNER_ID:
    LOGS.info("VRO ADD OWNER ID IN VARS")
    exit(1)


def connect_redis():
    yuvi = Config.REDIS_URI.split(":")
    op = StrictRedis(
        host=yuvi[0],
        port=yuvi[1],
        password=Config.REDIS_PASSWORD,
        charset="utf-8",
        decode_responses=True,
    )
    return op


try:
    db = connect_redis()
    LOGS.info("Connecting Db")
    time.sleep(6)
except ConnectionError as ce:
    LOGS.info(f"Error ~ {ce}")
    exit(1)
except ResponseError as re:
    LOGS.info(f"Error ~ {re}")
    exit(1)
except Exception as ex:
    LOGS.info(f"Error ~ {ex}")
    exit(1)

START_TIME = datetime.now()

try:
    db.ping()
except BaseException:
    ok = []
    LOGS.info("Can't connect to Database.... Restarting....")
    for x in range(1, 6):
        db = connect_redis()
        time.sleep(5)
        try:
            if db.ping():
                ok.append("ok")
                break
        except BaseException:
            LOGS.info(f"Database Connection Failed ...  Trying To Reconnect {x}/5 ..")
    if not ok:
        LOGS.info("Database Connection Failed.....")
        exit()
    else:
        LOGS.info("Reconnected To Server Succesfully")

LOGS.info("Succesfully Established Connection With DataBase.")
# Basics
APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
OWNER_ID = config("OWNER_ID", default=None)

xd = TelegramClient("xd", APP_ID, API_HASH).start(bot_token=BOT_TOKEN)

PLUGINS = []
