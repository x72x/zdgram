import aiohttp
import shitgram

from json import dumps

class GetMe:
    async def getMe(self: "shitgram.Bot") -> "shitgram.types.User":
        if "me" in self._cache_infos:
            return self._cache_infos['me']
        else:
            async with aiohttp.ClientSession() as client:
                async with client.post(
                    self.api.format(self.bot_token, "getMe"),
                ) as resp:
                    resp_json: dict = await resp.json()
                    if not resp_json.get("ok"):
                        raise shitgram.exceptions.ApiException(
                            dumps(resp_json, ensure_ascii=False)
                        )
                    me = shitgram.types.Update()._parse(shitgram.types.User()._parse(resp_json.get("result")))
                    self._cache_infos['me']=me
                    return me