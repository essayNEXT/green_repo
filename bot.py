import asyncio
import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from tgbot.config import BOT_TOKEN
# from tgbot.database.database import create_db

bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

# logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s] %(message)s',
#                     level=logging.INFO)
# storage = MemoryStorage()

# loop = asyncio.get_event_loop()

# db = loop.run_until_complete(create_db())  # створення db

if __name__ == "__main__":
    from tgbot.handlers.echo import dp, send_to_admin, on_shutdown

    executor.start_polling(dp, on_shutdown=on_shutdown, on_startup=send_to_admin)













# import asyncio
# import logging
#
# from aiogram import Bot, Dispatcher
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.contrib.fsm_storage.redis import RedisStorage2
#
# # from tgbot.config import load_config
# # from tgbot.filters.admin import AdminFilter
# # from tgbot.handlers.admin import register_admin
# from tgbot.handlers.echo import register_echo
# # from tgbot.handlers.user import register_user
# # from tgbot.middlewares.environment import EnvironmentMiddleware
#
# logger = logging.getLogger(__name__)
#
#
# # def register_all_middlewares(dp, config):
# #     dp.setup_middleware(EnvironmentMiddleware(config=config))
#
# #
# # def register_all_filters(dp):
# #     dp.filters_factory.bind(AdminFilter)
#
#
# def register_all_handlers(dp):
#     # register_admin(dp)
#     # register_user(dp)
#
#     register_echo(dp)
#
#
# async def main():
#     logging.basicConfig(
#         level=logging.INFO,
#         format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
#     )
#     logger.info("Starting bot")
#     config = load_config(".env")
#
#     storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage()
#     bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
#     dp = Dispatcher(bot, storage=storage)
#
#     bot['config'] = config
#
#     # register_all_middlewares(dp, config)
#     # register_all_filters(dp)
#     register_all_handlers(dp)
#
#     # start
#     try:
#         await dp.start_polling()
#     finally:
#         await dp.storage.close()
#         await dp.storage.wait_closed()
#         await bot.session.close()
#
#
# if __name__ == '__main__':
#     try:
#         asyncio.run(main())
#     except (KeyboardInterrupt, SystemExit):
#         logger.error("Bot stopped!")
