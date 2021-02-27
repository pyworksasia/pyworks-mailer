import os
from dotenv import load_dotenv
from pathlib import Path  # Python 3.6+ only

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Config:
    MAIL_HOST = os.getenv('MAIL_HOST')
    MAIL_PORT = os.getenv('MAIL_PORT')
    MAIL_TLS = os.getenv('MAIL_TLS', True)
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_RECEIVERS = os.getenv('MAIL_RECEIVERS')

    if MAIL_RECEIVERS is not None and MAIL_RECEIVERS.find(',') > -1:
        MAIL_RECEIVERS = MAIL_RECEIVERS.split(',')

config = Config()

