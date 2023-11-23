from json import dumps
from typing import Union, List

import zdgram

class SendPhoto:
    async def sendPhoto(
            self: "zdgram.Bot",
            chat_id: Union[int, str],
            photo: Union["zdgram.types.InputFile", str, bytes],
            caption: str = None,
            parse_mode: str = None,
            caption_entities: List["zdgram.types.MessageEntity"] = None,
            has_spoiler: bool = None,
            message_thread_id: int = None,
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
        Use this method to send photos. On success, the sent Message is returned.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param photo: Photo to send. Pass a file_id as String to send a photo that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a photo from the Internet, or upload a new photo using multipart/form-data. The photo must be at most 10 MB in size. The photo's width and height must not exceed 10000 in total. Width and height ratio must be at most 20. More information on Sending Files » https://core.telegram.org/bots/api#sending-files
        :param caption: Photo caption (may also be used when resending photos by file_id), 0-1024 characters after entities parsing
        :param parse_mode: Mode for parsing entities in the photo caption. See formatting options for more details. https://core.telegram.org/bots/api#formatting-options
        :param caption_entities: A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode
        :param has_spoiler: Pass True if the photo needs to be covered with a spoiler animation
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
        }
        is_file = False
        if isinstance(photo, str):
            data['photo']=photo
        elif isinstance(photo, zdgram.types.InputFile):
            is_file = True
        elif isinstance(photo, bytes):
            is_file = True
        if self.protect_content:
            data['protect_content']=self.protect_content
        if self.parse_mode:
            data['parse_mode']=self.parse_mode
        if self.disable_notification:
            data['disable_notification']=self.disable_notification
        if caption:
            data['caption']=caption
        if parse_mode is not None:
            data['parse_mode']=parse_mode
        if caption_entities:
            if isinstance(caption_entities[0], zdgram.types.MessageEntity):
                data['caption_entities']=dumps([i.__default__(i) for i in caption_entities])
            else:
                data['caption_entities']=dumps([i.__default__(i) for i in caption_entities])
        if has_spoiler:
            data['has_spoiler']=has_spoiler
        if message_thread_id:
            data['message_thread_id']=message_thread_id
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

        if is_file:
            resp_json = await self.sendRequest(
                method_name="sendPhoto",
                params=data,
                timeout=timeout,
                files={
                    "photo": photo
                }
            )
        else:
            resp_json = await self.sendRequest(
                method_name="sendPhoto",
                params=data,
                timeout=timeout
            )
        return zdgram.bot.update_manager._parse(zdgram.bot.message_manager._parse(resp_json.get("result")))

    send_photo = sendPhoto