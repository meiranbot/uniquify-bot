import os
import logging


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


class Config(object):
    # Get a bot token from @botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6022291124:AAG83L4MaW4aIpHQJKjzhGTZb89l5RuRCN0")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "10168777"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "bdc86ba6e1020f89dafa7944a726845d")

    # Authorized users to use this bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5948112774").split())

    # session name
    TG_USER_SESSION_NAME = os.environ.get("TG_USER_SESSION_NAME", "oxmohsen")

    # tg user session string
    TG_USER_SESSION_STRING = os.environ.get("TG_USER_SESSION_STRING", "1BVtsOLUBu12wnbAWA2VBciT9pSs2K5-WmPpfYv_FFzAoi6i97YZUCdHlwiBMeV--0PzHQQ0f-m9uPwVF9ZOxKW4OsBiDisI-OPYWY4EhLPHEPYOFd0GbFnmo5dlFaLWjxGLI-Oh5IjsWqDJUuUywcpMT5gqO9arfoQ4-980klkSz5fSLCEApvLPfIDlFs8EIP8yEoF6iF6Tr6O14MEc0gqVDrtRrwBIrM-lAtydUm2Nhhn3Xgpia1kIKFWyTvrsjJF3GFkiKEYzZNo03a2yVZIySOmXRwTV3LfwYN7XnuBAxApErMpVYD6_9a0FpHRewbxd8jTm5E7PLa7hTHxWG8ZhNvkLWyIw=")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
