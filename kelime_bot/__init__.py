from time import sleep
from pyrogram import Client
import logging
from dotenv import load_dotenv, set_key, unset_key
from os import getenv

load_dotenv('config.env')

# THE LOGGING
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)


# Hesap
API_ID = getenv("API_ID", "9248715")
API_HASH = getenv("API_HASH", "a9c1288681c2d3265175ff96c619d064")
TOKEN = getenv("TOKEN", "5510555268:AAEIYUALuPpZN41CdLS4xjuC_L2q6nzKOVk")
USERNAME = getenv("USERNAME", "SharkGameBot")
OWNER_ID = getenv("OWNER_ID", "5784013817")

if OWNER_ID and len(OWNER_ID) and OWNER_ID.isdigit():
    OWNER_ID = int(OWNER_ID)  # type: ignore
else:
    OWNER_ID = None  # type: ignore

# BOT CLIENTİ
bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=TOKEN,
    plugins=dict(root="kelime_bot/plugins/"),
    workers=16
)


# Oyun Verileri
oyun = {}  # type: ignore


# rating
rating = {}  # type: ignore



if __name__ == "__init__":
    bot.run()
