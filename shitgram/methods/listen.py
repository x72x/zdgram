import shitgram
import asyncio

class Listener:
    async def Listen(self: "shitgram.Bot", func: any) -> "shitgram.types.Message":
        self.add_listen_handler(func)
        loop = asyncio.get_event_loop()
        def _():
            while func in self._listener:
                pass
            return self._listener_cache[id(func)]

        return await loop.run_in_executor(
            None, _
        )

    listen = Listen