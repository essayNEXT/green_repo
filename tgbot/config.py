import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
admin_id = str(os.getenv("ADMINS"))

PGUSER = str(os.getenv("PGUSER"))
PGPASSWORD = str(os.getenv("PG_PASSWORD"))
host = str(os.getenv("PG_HOST"))









# DATABASE = str(os.getenv("DATABASE"))
#
#
# ip = os.getenv("ip")
#
# POSTGRESURI = f"postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}"
#
# aiogram_redis = {
#     'host': ip,
# }









# from dataclasses import dataclass
#
# from environs import Env
#
#
# @dataclass
# class DbConfig:
#     host: str
#     password: str
#     user: str
#     database: str
#
#
# @dataclass
# class TgBot:
#     token: str
#     admin_ids: list[int]
#     use_redis: bool
#
#
# @dataclass
# class Miscellaneous:
#     other_params: str = None
#
#
# @dataclass
# class Config:
#     tg_bot: TgBot
#     db: DbConfig
#     misc: Miscellaneous
#
#
# def load_config(path: str = None):
#     env = Env()
#     env.read_env(path)
#
#     return Config(
#         tg_bot=TgBot(
#             token=env.str("BOT_TOKEN"),
#             admin_ids=list(map(int, env.list("ADMINS"))),
#             use_redis=env.bool("USE_REDIS"),
#         ),
#         db=DbConfig(
#             host=env.str('DB_HOST'),
#             password=env.str('DB_PASS'),
#             user=env.str('DB_USER'),
#             database=env.str('DB_NAME')
#         ),
#         misc=Miscellaneous()
#     )
