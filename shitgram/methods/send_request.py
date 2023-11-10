import shitgram
import aiohttp

class SendRequest:
    async def sendRequest(self: "shitgram.Bot", method_name: str, params: dict = None) -> dict:
        session = await shitgram.bot.session_manager.get_session()
        async with session.request(
            method="post",
            url=self.api.format(self.bot_token, method_name),
            data=params,
            timeout=aiohttp.ClientTimeout(total=300)
        ) as resp:
                return await resp.json()