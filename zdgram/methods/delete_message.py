import zdgram
from typing import Union

class DeleteMessage:
    async def deleteMessage(
            self: "zdgram.Bot",
            chat_id: Union[str, int],
            message_id: int,
            timeout: int = None
    ) -> bool:
        """
        Use this method to delete a message, including service messages, with the following limitations:
        - A message can only be deleted if it was sent less than 48 hours ago.
        - Service messages about a supergroup, channel, or forum topic creation can't be deleted.
        - A dice message in a private chat can only be deleted if it was sent more than 24 hours ago.
        - Bots can delete outgoing messages in private chats, groups, and supergroups.
        - Bots can delete incoming messages in private chats.
        - Bots granted can_post_messages permissions can delete outgoing messages in channels.
        - If the bot is an administrator of a group, it can delete any message there.
        - If the bot has can_delete_messages permission in a supergroup or a channel, it can delete any message there.

        Args:

            chat_id (`Union[str, int]`): Unique identifier for the target chat or username of the target channel (in the format @channelusername)

            message_id (`int`): Identifier of the message to delete

        Returns:

            bool: Returns True on success

        Example:
            ```
            await bot.deleteMessage(chat_id, message_id)
            ```
        """
        return (
            await self.sendRequest(
                "deleteMessage",
                {
                    "chat_id": chat_id,
                    "message_id": message_id
                },
                timeout=timeout
            )
        ).get("result")

    delete_message = deleteMessage