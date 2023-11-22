import zdgram

from typing import Union

class ForwardMessage:
    async def forwardMessage(
            self: "zdgram.Bot",
            chat_id: Union[int, str],
            from_chat_id: Union[int, str],
            message_id: int,
            message_thread_id: int = None,
            disable_notification: bool = None,
            protect_content: bool = None,
            timeout: int = None
    ) -> "zdgram.types.Message":
        """
        Use this method to forward messages of any kind. Service messages can't be forwarded. On success, the sent Message is returned.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param from_chat_id: Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername)
        :param message_id: Message identifier in the chat specified in from_chat_id
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :param protect_content: Protects the contents of the forwarded message from forwarding and saving
        :param timeout: Request TimeOut
        :return: On success, the sent Message is returned.
        """
        data = {
            'chat_id': chat_id,
            'from_chat_id': from_chat_id,
            'message_id': message_id
        }
        if self.protect_content:
            data['protect_content']=self.protect_content
        if self.disable_notification:
            data['disable_notification']=self.disable_notification
        if message_thread_id:
            data['message_thread_id']=message_thread_id
        if disable_notification is not None:
            data['disable_notification']=disable_notification
        if protect_content is not None:
            data['protect_content']=protect_content

        resp_json = await self.sendRequest(
            method_name="forwardMessage",
            params=data,
            timeout=timeout
        )
        return zdgram.bot.update_manager._parse(zdgram.bot.message_manager._parse(resp_json.get("result")))

    forward_message = forwardMessage