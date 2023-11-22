import zdgram

class LogOut:
    async def logOut(self: "zdgram.Bot"):
        """
        Use this method to log out from the cloud Bot API server before launching the bot locally. You must log out the bot before running it locally, otherwise there is no guarantee that the bot will receive updates. After a successful call, you can immediately log in on a local server, but will not be able to log in back to the cloud Bot API server for 10 minutes. Returns True on success. Requires no parameters.

        :return:  Returns True on success
        """
        await self.sendRequest(
            method_name="logOut"
        )
        return True

    log_out = logOut