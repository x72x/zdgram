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
        self.cache = []
        self.funcs = []
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
                        if not self.cache:
                            self.cache.append(update.get("update_id"))
                            logging.info("getUpdates running now")
                            continue
                        if update.get("update_id") not in self.cache:
                            self.cache.append(update.get("update_id"))
                            for func in self.funcs:
                                await self.loop.run_in_executor(
                                    None,
                                    func=lambda: self.loop.create_task(func(self, Update()._parse(update)))
                                )

    @property
    def on_update(self):
        def decorator(func: Callable) -> Callable:
            self.add_handler(func)

        return decorator

    def add_handler(self, func: Callable) -> Callable:
        self.funcs.append(func)

    def start_polling(self, allowed_updates: list = None):
        if allowed_updates:
            self.getUpdatesData['allowed_updates'] = allowed_updates
        self.loop.create_task(self.get_updates())
        self.loop.run_forever()