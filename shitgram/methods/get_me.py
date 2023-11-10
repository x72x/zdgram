import aiohttp
import shitgram

from json import dumps

class GetMe:
    async def getMe(self: "shitgram.Bot") -> "shitgram.types.User":
        if "me" in self.cache:
            return self.cache.get('me')
        resp_json = await self.sendRequest(
            method_name="getMe"
        )
        if not resp_json.get("ok"):
            raise shitgram.exceptions.ApiException(
                dumps(resp_json, ensure_ascii=False)
            )
        me = shitgram.types.Update()._parse(shitgram.types.User()._parse(resp_json.get("result")))
        self.cache.update({"me": me})
        return me