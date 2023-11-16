import shitgram

class LogOut:
    async def logOut(self: "shitgram.Bot"):
        await self.sendRequest(
            method_name="logOut"
        )
        return True