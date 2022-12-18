import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
class Config(object):
    log = True
    APP_ID = getenv("API_ID", "21967179")
    API_HASH = getenv("API_HASH", "37d5fbb9217cb56d6261e61305d92748")
    TOKEN = getenv("TOKEN", "5835236187:AAFP4OxZVBhrTxsmjjm6p-CAuA3qwLR_4g4")
    OWNER_ID = getenv("OWNER_ID", "5530347700")
    ASSISTANT_ID = getenv("ASSISTANT_ID", "")
    STRING_SESSION = getenv("STRING_SESSION", "")
    OWNER_USERNAME = getenv("OWNER_USERNAME", "kailas_vg")
    DB_URI = getenv("DATABASE_URL", "")
    DB_URI = DB_URI.replace("postgres", "postgresql")
    MESSAGE_DUMP = getenv("MESSAGE_DUMP", "-1001750486845")
    GBAN_LOGS = getenv("GBAN_LOGS", "-1001750486845")
    SYS_ADMIN = getenv("SYS_ADMIN", "5428019786")
    DEV_USERS = getenv("DEV_USERS", "5428019786")
    LOAD = getenv("LOAD")
    WEBHOOK = False
    SPB_MODE = True
    DROP_UPDATES = False
    DEBUG = False
    URL = None
    INFOPIC = True
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    BAN_STICKER = getenv("BAN_STICKER", "")
    ALLOW_EXCL = True
    CUSTOM_CMD = False
    CHANNEL = getenv("CHANNEL", "About_kailas")
    SUPPORT = getenv("SUPPORT", "Pranav_support_Chat")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    CASH_API_KEY = getenv("CASH_API_KEY", "https://www.alphavantage.co/support/#api-key")
    TIME_API_KEY = getenv("TIME_API_KEY", "https://timezonedb.com/api")
    WALL_API = getenv("WALL_API", "https://wall.alphacoders.com/api.php")
    spamwatch_api = getenv("spamwatch_api", "https://t.me/SpamWatchBot")
    SPAMMERS = getenv("SPAMMERS", "")
    LASTFM_API_KEY = getenv("LASTFM_API_KEY", "https://www.last.fm/api/account/create")
    CF_API_KEY = getenv("CF_API_KEY", "coffehouse.intellivoid.net")
    BOT_API_URL = getenv("BOT_API_URL", "https://api.telegram.org/bot")
    BOT_API_FILE_URL = getenv("BOT_API_FILE_URL", "https://api.telegram.org/file/bot")
    SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5428019786").split()))
    ZAID_USER = list(map(int, getenv("DEV_USERS", "5428019786").split()))
    NO_LOAD = list(map(int, getenv("NO_LOAD", "").split()))
