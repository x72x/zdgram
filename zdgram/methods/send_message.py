from json import dumps
from typing import Union, List

import zdgram

class SendMessage:
    async def sendMessage(
            self: "zdgram.Bot",
            chat_id: Union[int, str],
            text: str,
            parse_mode: str = None,
            message_thread_id: int = None,
            entities: List["zdgram.types.MessageEntity"] = None,
            disable_web_page_preview: bool = None,
            disable_notification: bool = None,
            protect_content: bool = None,
            reply_to_message_id: int = None,
            allow_sending_without_reply: bool = None,
            reply_markup: Union[
                "zdgram.types.InlineKeyboardMarkup",
                "zdgram.types.ForceReply",
                "zdgram.types.ReplyKeyboardMarkup",
                "zdgram.types.ReplyKeyboardRemove"
            ] = None,
            timeout: int = None
    ) -> "zdgram.types.Message":
        """
        Use this method to send text messages. On success, the sent Message is returned.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param text: Text of the message to be sent, 1-4096 characters after entities parsing
        :param parse_mode: Mode for parsing entities in the message text. See formatting options for more details. https://core.telegram.org/bots/api#formatting-options
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
        :param disable_web_page_preview: Disables link previews for links in this message
        :param entities: A JSON-serialized list of special entities that appear in message text, which can be specified instead of parse_mode
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
            'text': text
        }
        if self.protect_content:
            data['protect_content']=self.protect_content
        if self.parse_mode:
            data['parse_mode']=self.parse_mode
        if self.disable_notification:
            data['disable_notification']=self.disable_notification
        if self.disable_web_page_preview:
            data['disable_web_page_preview']=self.disable_web_page_preview
        if message_thread_id:
            data['message_thread_id']=message_thread_id
        if parse_mode is not None:
            data['parse_mode']=parse_mode
        if entities:
            data['entities']=dumps([str(i) if isinstance(i, zdgram.types.MessageEntity) else i.__dict__.get("_DictionaryToClass__dict") for i in entities])
        if disable_web_page_preview is not None:
            data['disable_web_page_preview']=disable_web_page_preview
        if disable_notification is not None:
            data['disable_notification']=disable_notification
        if protect_content is not None:
            data['protect_content']=protect_content
        if reply_to_message_id:
            data['reply_to_message_id']=reply_to_message_id
        if allow_sending_without_reply:
            data['allow_sending_without_reply']=allow_sending_without_reply
        if reply_markup:
            data['reply_markup']=zdgram.utils.reply_markup_parse(reply_markup)

        resp_json = await self.sendRequest(
            method_name="sendMessage",
            params=data,
            timeout=timeout
        )
        return zdgram.bot.update_manager._parse(zdgram.bot.message_manager._parse(resp_json.get("result")))

    send_message = sendMessage