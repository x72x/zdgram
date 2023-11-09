import aiohttp
import asyncio
import logging

from typing import Callable
from .methods import Methods
from .types import Update

API_URL = "https://api.telegram.org/bot{}/{}"

class Bot(Methods):
    def __init__(self, bot_token: str, api_url: str = None) -> None:
        self.bot_token = bot_token
        self.__cache = []
        self.__funcs = []
        self.__message_handlers = []
        self.__edited_message_handlers = []
        self.__callback_query_handlers = []
        self.__cache_infos = {}
        self.api = api_url or API_URL

        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

        self.loop = loop
        self.getUpdatesData = {
            "offset": -1,
            "timeout": 600
        }

    async def get_updates(self):
        while True:
            async with aiohttp.ClientSession() as client:
                async with client.post(
                    API_URL.format(self.bot_token, "getUpdates"),
                    data=self.getUpdatesData
                ) as resp:
                    updates = await resp.json()
                    for update in updates.get("result"):
                        if not self.__cache:
                            self.__cache.append(update.get("update_id"))
                            logging.info("getUpdates running now")
                            continue
                        if update.get("update_id") not in self.__cache:
                            self.__cache.append(update.get("update_id"))
                            upd = Update()._parse(update)
                            for func in self.__funcs:
                                await self.loop.run_in_executor(
                                    None,
                                    func=lambda: self.loop.create_task(func(self, upd))
                                )

                            if upd.message and not upd.message.edit_date:
                                for func in self.__message_handlers:
                                    if (func['filter_func']) and not func['filter_func'](upd.message):
                                        continue
                                    else:
                                        await self.loop.run_in_executor(
                                            None,
                                            func=lambda: self.loop.create_task(func['func'](self, upd.message))
                                        )

                            if upd.message and upd.message.edit_date:
                                for func in self.__edited_message_handlers:
                                    if (func['filter_func']) and not func['filter_func'](upd.message):
                                        continue
                                    else:
                                        await self.loop.run_in_executor(
                                            None,
                                            func=lambda: self.loop.create_task(func['func'](self, upd.message))
                                        )

                            if upd.callback_query:
                                for func in self.__callback_query_handlers:
                                    if (func['filter_func']) and not func['filter_func'](upd.callback_query):
                                        continue
                                    else:
                                        await self.loop.run_in_executor(
                                            None,
                                            func=lambda: self.loop.create_task(func['func'](self, upd.callback_query))
                                        )


    async def auto_clean_cache(self):
        while not await asyncio.sleep(500):
            self.__cache_infos.clear()

    @property
    def onUpdate(self):
        def decorator(func: Callable) -> Callable:
            self.add_any_update_handler(func)

        return decorator

    def onMessage(self, func: Callable = None):
        def decorator(func_: Callable) -> Callable:
            self.add_message_handler(func_, func)

        return decorator

    def onEditedMessage(self, func: Callable = None):
        def decorator(func_: Callable) -> Callable:
            self.add_edited_message_handler(func_, func)

        return decorator

    def onCallbackQuery(self, func: Callable = None):
        def decorator(func_: Callable) -> Callable:
            self.add_callback_query_handler(func_, func)

        return decorator

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

    def start_polling(self, allowed_updates: list = None):
        if allowed_updates:
            self.getUpdatesData['allowed_updates'] = allowed_updates
        self.loop.create_task(self.get_updates())
        self.loop.create_task(self.auto_clean_cache())
        self.loop.run_forever()