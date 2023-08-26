import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass
class TgBot:
    token: str
    admin_ids: int


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    load_dotenv()
    return Config(tg_bot=TgBot(
        token=os.getenv('BOT_TOKEN'),
        admin_ids=int(os.getenv('ADMIN_IDS'))
    ))
