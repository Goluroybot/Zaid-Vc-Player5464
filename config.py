## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("TELETHON")

if str(getenv("STRING_SESSION2")).strip() == "1AZWarzsBu2Yq2VWPMpHBrxWHURVwQRZnoa2QeapLC-gsjeZxdXX9XaBpiv4yBzlSQ12jtzvpg9YlruPg0UVcsKeWIInOx6eBm-JVO5Gl3FgrAmEiQ8K-ie_n6_VDQf9_-QWssNBNxmLtW4WhVsNCgMxhs29eZGhFp7BTfoJilefT2uYwO1i7iDCJVX5RC47kZZ1strNBSBny0m8s5R9a85HjFDYP8YrWY-BBTj4bn8NZ0Cycg-0nXW8L5HjzqGWryWY-NBJvuITdQUyfAccKPum51rlIb2LVyZlYqn5GuJVry9YWHZ3HEfu5cw5BnKoRluAtYd-BbiixfekPT9-Pu2hT0qNMrPM=":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "5930549721:AAGQGXPDFDQLZQrnmAJuZK595EMTeucb930")
BOT_NAME = getenv("BOT_NAME", "hjjj")

API_ID = int(getenv("API_ID", "27633466")
API_HASH = getenv("API_HASH", "bb85d45cfcdf015bd7691075045ab723")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb://ud7kcz6totsvepy86bb2:d4gmTfoBbpzDmNLzItwG@n1-c2-mongodb-clevercloud-customers.services.clever-cloud.com:27017,n2-c2-mongodb-clevercloud-customers.services.clever-cloud.com:27017/b0ojwj6pcvvj30u?replicaSet=rs0")
OWNER_NAME = getenv("OWNER_NAME", "ABHI ROY")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ANUJ_Assistant")
ALIVE_NAME = getenv("ALIVE_NAME", "ABHI ROY")
BOT_USERNAME = getenv("BOT_USERNAME", "ANUJ2_Robot")
OWNER_ID = getenv("OWNER_ID", "5830584815")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "ANUJ_Assistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "+ft7zGtQVxhhiYzFl)
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "+QwEx_yTl2igwZDRh")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5830584815").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ABHI/ANUJ_BOT")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/10b1f781170b1e1867f68.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
HEROKU_MODE = getenv("HEROKU_MODE", None)
