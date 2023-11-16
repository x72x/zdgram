import shitgram

from json import dumps

class GetMe:
    async def getMe(self: "shitgram.Bot") -> "shitgram.types.User":
        if "me" in self.cache:
            return self.cache.get('me')
        resp_json = await self.sendRequest(
            method_name="getMe"
        )
        me = shitgram.types.Update()._parse(shitgram.types.User()._parse(resp_json.get("result")))
        self.cache.update({"me": me})
        return me