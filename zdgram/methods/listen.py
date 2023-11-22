import zdgram
import asyncio

class Listener:
    async def Listen(self: "zdgram.Bot", func: any) -> "zdgram.types.Message":
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