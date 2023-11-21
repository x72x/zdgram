import shitgram

from typing import Union, List
from json import dumps

class CopyMessage:
    async def copyMessage(
            self: "shitgram.Bot",
            chat_id: Union[int, str],
            from_chat_id: Union[int, str],
            message_id: int,
            caption: str = None,
            parse_mode: str = None,
            caption_entities: List["shitgram.types.MessageEntity"] = None,
            reply_to_message_id: int = None,
            message_thread_id: int = None,
            disable_notification: bool = None,
            protect_content: bool = None,
            allow_sending_without_reply: bool = None,
            reply_markup: Union[
                "shitgram.types.InlineKeyboardMarkup",
                "shitgram.types.ForceReply",
                "shitgram.types.ReplyKeyboardMarkup",
                "shitgram.types.ReplyKeyboardRemove"
            ] = None,
            timeout: int = None
    ) -> "shitgram.types.Message":
        """
        Use this method to copy messages of any kind. Service messages and invoice messages can't be copied. A quiz poll can be copied only if the value of the field correct_option_id is known to the bot. The method is analogous to the method forwardMessage, but the copied message doesn't have a link to the original message. Returns the MessageId of the sent message on success.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param from_chat_id: Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername)
        :param message_id: Message identifier in the chat specified in from_chat_id
        :param caption: New caption for media, 0-1024 characters after entities parsing. If not specified, the original caption is kept
        :param parse_mode: Mode for parsing entities in the new caption. See formatting options for more details. https://core.telegram.org/bots/api#formatting-options
        :param caption_entities: A JSON-serialized list of special entities that appear in the new caption, which can be specified instead of parse_mode
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :param protect_content: Protects the contents of the sent message from forwarding and saving
        :param reply_to_message_id: If the message is a reply, ID of the original message
        :param allow_sending_without_reply: Pass True if the message should be sent even if the specified replied-to message is not found
        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
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
        if self.parse_mode:
            data['parse_mode']=self.parse_mode
        if self.disable_notification:
            data['disable_notification']=self.disable_notification
        if message_thread_id:
            data['message_thread_id']=message_thread_id
        if parse_mode is not None:
            data['parse_mode']=parse_mode
        if caption:
            data['caption']=caption
        if caption_entities:
            data['caption_entities']=dumps([i.__dict__.get("_dtc__dict") for i in caption_entities], ensure_ascii=False)
        if disable_notification is not None:
            data['disable_notification']=disable_notification
        if protect_content is not None:
            data['protect_content']=protect_content
        if reply_to_message_id:
            data['reply_to_message_id']=reply_to_message_id
        if allow_sending_without_reply:
            data['allow_sending_without_reply']=allow_sending_without_reply
        if reply_markup:
            data['reply_markup']=shitgram.utils.reply_markup_parse(reply_markup)

        resp_json = await self.sendRequest(
            method_name="copyMessage",
            params=data,
            timeout=timeout
        )
        return shitgram.bot.update_manager._parse(shitgram.bot.message_manager._parse(resp_json.get("result")))

    copy_message = copyMessage