# Test configuration

from mailer.config import config


class TestConfig:

    # def __init__(self) -> None:
    #     self.config = Config()

    def test_config(self):
        assert hasattr(config, 'MAIL_HOST')