import aiohttp
import asyncio
import logging
import ssl
import certifi

from typing import Callable
from .methods import Methods
from .types import Update
from .handlers import Handlers

API_URL = "https://api.telegram.org/bot{}/{}"

class SessionManager:
    # https://github.com/eternnoir/pyTelegramBotAPI/blob/f91f42321c95e0cedda483ba5442e0b4eee057c5/telebot/asyncio_helper.py#L31
    def __init__(self) -> None:
        self.session = None
        self.ssl_context = ssl.create_default_context(cafile=certifi.where())


    async def create_session(self):
        self.session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(
            limit=50,
            ssl_context=self.ssl_context
        ))
        return self.session

    async def get_session(self):
        if self.session is None:
            self.session = await self.create_session()
            return self.session

        if self.session.closed:
            self.session = await self.create_session()

        # noinspection PyProtectedMember
        if not self.session._loop.is_running():
            await self.session.close()
            self.session = await self.create_session()
        return self.session


session_manager = SessionManager()

class Bot(Methods, Handlers):
    def __init__(self, bot_token: str, api_url: str = None) -> None:
        self.bot_token = bot_token
        self.__cache = []
        self.__funcs = []
        self.__message_handlers = []
        self.__edited_message_handlers = []
        self.__callback_query_handlers = []
        self.__channel_post_handlers = []
        self.__edited_channel_post_handlers = []
        self.cache = {}
        self.api = api_url or API_URL

        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

        self.loop = loop
        self.getUpdatesData = {
            "offset": -1,
        }

    async def get_updates(self):
        while True:
            updates = await self.sendRequest(
                method_name="getUpdates",
                params=self.getUpdatesData
            )
            for update in updates.get("result"):
                if not self.__cache:
                    self.__cache.append(update.get("update_id"))
                    logging.info("getUpdates running now")
                    continue
                if update.get("update_id") not in self.__cache:
                    self.__cache.append(update.get("update_id"))
                    upd = Update()._parse(update)
                    for func in self.__funcs:
                        self.loop.create_task(func['func'](self, upd))
                    if update.get("message"):
                        for func in self.__message_handlers:
                            if (func['filter_func']) and not func['filter_func'](upd.message):
                                continue
                            else:
                                self.loop.create_task(func['func'](self, upd.message))
                    if update.get("edited_message"):
                        for func in self.__edited_message_handlers:
                            if (func['filter_func']) and not func['filter_func'](upd.message):
                                continue
                            else:
                                self.loop.create_task(func['func'](self, upd.message))
                    if update.get("callback_query"):
                        for func in self.__callback_query_handlers:
                            if (func['filter_func']) and not func['filter_func'](upd.callback_query):
                                continue
                            else:
                                self.loop.create_task(func['func'](self, upd.callback_query))
                    if update.get("channel_post"):
                        for func in self.__channel_post_handlers:
                            if (func['filter_func']) and not func['filter_func'](upd.message):
                                continue
                            else:
                                self.loop.create_task(func['func'](self, upd.message))
                    if update.get("edited_channel_post"):
                        for func in self.__edited_channel_post_handlers:
                            if (func['filter_func']) and not func['filter_func'](upd.message):
                                continue
                            else:
                                self.loop.create_task(func['func'](self, upd.message))

    async def auto_clean_cache(self):
        while not await asyncio.sleep(500):
            self.cache.clear()

    def add_any_update_handler(self, func: Callable) -> Callable:
        self.__funcs.append(func)

    def add_callback_query_handler(self, func_: Callable, func: Callable = None) -> Callable:
        self.__callback_query_handlers.append(
            {
                "func": func_,
                "filter_func": func
            }
        )

    def add_edited_message_handler(self, func_: Callable, func: Callable = None) -> Callable:
        self.__edited_message_handlers.append(
            {
                "func": func_,
                "filter_func": func
            }
        )

    def add_message_handler(self, func_: Callable, func: Callable = None) -> Callable:
        self.__message_handlers.append(
            {
                "func": func_,
                "filter_func": func
            }
        )

    def add_channel_post_handler(self, func_: Callable, func: Callable = None) -> Callable:
        self.__channel_post_handlers.append(
            {
                "func": func_,
                "filter_func": func
            }
        )

    def add_edited_channel_post_handler(self, func_: Callable, func: Callable = None) -> Callable:
        self.__edited_channel_post_handlers.append(
            {
                "func": func_,
                "filter_func": func
            }
        )

    def start_polling(self, allowed_updates: list = None):
        if allowed_updates:
            self.getUpdatesData['allowed_updates'] = allowed_updates
        self.loop.create_task(self.get_updates())
        self.loop.create_task(self.auto_clean_cache())
        self.loop.run_forever()