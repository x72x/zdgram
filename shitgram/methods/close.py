import shitgram

class Close:
    async def close(self: "shitgram.Bot"):
        await self.sendRequest(
            "close"
        )
        return True