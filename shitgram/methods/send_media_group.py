import shitgram
from typing import Union, List
from json import dumps

class SendMediaGroup:
    async def sendMediaGroup(
            self: "shitgram.Bot",
            chat_id: Union["str", "int"],
            media: List[
                Union[
                    "shitgram.types.InputMediaPhoto",
                    "shitgram.types.InputMediaVideo",
                    "shitgram.types.InputMediaAudio",
                    "shitgram.types.InputMediaAnimation",
                    "shitgram.types.InputMediaDocument"
                ]
            ],
            message_thread_id: int = None,
            disable_notification: bool = None,
            protect_content: bool = None,
            reply_to_message_id: int = None,
            allow_sending_without_reply: bool = None,
            timeout: int = None,
    ) -> List["shitgram.types.Message"]:
        """
        Use this method to send a group of photos, videos, documents or audios as an album. Documents and audio files can be only grouped in an album with messages of the same type. On success, an array of Messages that were sent is returned.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param media: A JSON-serialized array describing messages to be sent, must include 2-10 items
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
        :param disable_notification: Sends messages silently. Users will receive a notification with no sound.
        :param protect_content: Protects the contents of the sent messages from forwarding and saving
        :param reply_to_message_id: If the messages are a reply, ID of the original message
        :param allow_sending_without_reply: Pass True if the message should be sent even if the specified replied-to message is not found
        :param timeout: Request TimeOut
        :return: On success, an array of Messages that were sent is returned.
        """
        if self.protect_content and protect_content is None:
            protect_content=self.protect_content
        if self.disable_notification and disable_notification is None:
            disable_notification=self.disable_notification
        result = await shitgram.utils.send_media_group(
            self,
            chat_id=chat_id,
            media=media,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply,
            message_thread_id=message_thread_id,
            timeout=timeout
        )
        return [shitgram.bot.update_manager._parse(shitgram.bot.message_manager._parse(i)) for i in result.get("result")]

    send_media_group = sendMediaGroup