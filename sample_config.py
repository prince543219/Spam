from os import environ as env

from dotenv import load_dotenv

load_dotenv("config.env")

"""
READ EVERYTHING CAREFULLY!!!
"""


DEPLOYING_ON_HEROKU = (
    True  # Make this False if you're not deploying On heroku/Docker
)


if not DEPLOYING_ON_HEROKU:
    BOT_TOKEN = "7955007597:AAGWneTp9e-l4iXE0Zxvh2-4-OFgjdUbi9s"
    SUDOERS = [6375272628]
    NSFW_LOG_CHANNEL = -1002107679944
    SPAM_LOG_CHANNEL = -1002107679944
    ARQ_API_KEY = "IKIQKD-JTNSIW-VPZJSR-ZKVOGR-ARQ"  # Get it from @ARQRobot
else:
    BOT_TOKEN = env.get("BOT_TOKEN")
    SUDOERS = [int(x) for x in env.get("SUDO_USERS_ID", "6375272628").split()]
    NSFW_LOG_CHANNEL = int(env.get("NSFW_LOG_CHANNEL"))
    SPAM_LOG_CHANNEL = int(env.get("SPAM_LOG_CHANNEL"))
    ARQ_API_KEY = env.get("ARQ_API_KEY")
