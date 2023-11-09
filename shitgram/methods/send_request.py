import shitgram
import aiohttp

class SendRequest:
    async def sendRequest(self: "shitgram.Bot", method_name: str, params: dict = None) -> dict:
        async with aiohttp.ClientSession() as client:
            async with client.post(
                self.api.format(self.bot_token, method_name),
                data=params
            ) as resp:
                return await resp.json()