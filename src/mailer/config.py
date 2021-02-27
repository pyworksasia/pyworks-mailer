import os
from utils import scandir
from dotenv import load_dotenv
from pathlib import Path  # Python 3.6+ only

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Config(object):

    def __init__(self):
        self.MAIL_PROVIDER_SUPPORTED = ['gmail', 'yandex', 'ses']
        self.MAIL_PROVIDER = os.getenv('MAIL_PROVIDER')
        self.MAIL_HOST = os.getenv('MAIL_HOST')
        self.MAIL_PORT = os.getenv('MAIL_PORT')
        self.MAIL_TLS = os.getenv('MAIL_TLS', True)
        self.MAIL_USERNAME = os.getenv('MAIL_USERNAME')
        self.MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
        self.MAIL_RECEIVERS = os.getenv('MAIL_RECEIVERS')

        if self.MAIL_RECEIVERS is not None and self.MAIL_RECEIVERS.find(',') > -1:
            self.MAIL_RECEIVERS = self.MAIL_RECEIVERS.split(',')

        self.MAIL_TEMPLATES_ROOT = 'templates'
        self.MAIL_TEMPLATES = scandir(f'{os.getcwd()}/{self.MAIL_TEMPLATES_ROOT}')

config = Config()
# print(config)

