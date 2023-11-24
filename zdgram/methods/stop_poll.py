import zdgram
from typing import Union

class StopPoll:
    async def stopPoll(
            self: "zdgram.Bot",
            chat_id: Union[int, str],
            message_id: int,
            reply_markup: "zdgram.types.InlineKeyboardMarkup" = None,
            timeout: int = None
    ) -> "zdgram.types.Poll":
        """Use this method to stop a poll which was sent by the bot. On success, the stopped Poll is returned.
        https://core.telegram.org/bots/api#stoppoll

        Args:

            chat_id (`Union[int, str]`): Unique identifier for the target chat or username of the target channel (in the format @channelusername)

            message_id (`int`): Identifier of the original message with the poll

            reply_markup (`zdgram.types.InlineKeyboardMarkup`, optional): A JSON-serialized object for a new message inline keyboard.. Defaults to None.

        Returns:

            zdgram.types.Poll: On success, the stopped Poll is returned.

        Example:

            ```
            await bot.stopPoll(
                chat_id,
                message_id
            )
            ```
        """
        data = {
            "chat_id": chat_id,
            "message_id": message_id
        }
        if reply_markup:
            data["reply_markup"]=zdgram.utils.reply_markup_parse(reply_markup)

        response = await self.sendRequest(
            "stopPoll",
            params=data,
            timeout=timeout
        )
        return zdgram.bot.update_manager._parse(response)

    stop_poll = stopPoll