from json import dumps
from typing import Union, List

import shitgram

class SendVoice:
    async def sendVoice(
            self: "shitgram.Bot",
            chat_id: Union[int, str],
            voice: Union["shitgram.types.InputFile", str, bytes],
            caption: str = None,
            parse_mode: str = None,
            caption_entities: List["shitgram.types.MessageEntity"] = None,
            duration: int = None,
            message_thread_id: int = None,
            disable_notification: bool = None,
            protect_content: bool = None,
            reply_to_message_id: int = None,
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
        Use this method to send audio files, if you want Telegram clients to display the file as a playable voice message. For this to work, your audio must be in an .OGG file encoded with OPUS (other formats may be sent as Audio or Document). On success, the sent Message is returned. Bots can currently send voice messages of up to 50 MB in size, this limit may be changed in the future.


        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param voice: Audio file to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data.
        :param caption: Voice message caption, 0-1024 characters after entities parsing
        :param parse_mode: Mode for parsing entities in the voice message caption.
        :param caption_entities: A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode
        :param duration: Duration of the voice message in seconds
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :param protect_content: Protects the contents of the sent message from forwarding and saving
        :param reply_to_message_id: If the message is a reply, ID of the original message
        :param allow_sending_without_reply: Pass True if the message should be sent even if the specified replied-to message is not found
        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
        :param timeout: Request TimeOut
        :return: On success, the sent Message is returned. Bots can currently send voice messages of up to 50 MB in size, this limit may be changed in the future.
        """
        data = {
            'chat_id': chat_id,
        }
        is_file = False
        if isinstance(voice, str):
            data['voice']=voice
        elif isinstance(voice, shitgram.types.InputFile):
            is_file = True
        elif isinstance(voice, bytes):
            is_file = True
        if caption:
            data['caption']=caption
        if parse_mode:
            data['parse_mode']=parse_mode
        if caption_entities:
            if isinstance(caption_entities[0], shitgram.types.MessageEntity):
                data['caption_entities']=dumps([i.__dict__ for i in caption_entities], ensure_ascii=False)
            else:
                data['caption_entities']=dumps([i.__dict__.get("_DictionaryToClass__dict") for i in caption_entities], ensure_ascii=False)
        if duration:
            data["duration"]=duration
        if message_thread_id:
            data['message_thread_id']=message_thread_id
        if disable_notification:
            data['disable_notification']=disable_notification
        if protect_content:
            data['protect_content']=protect_content
        if reply_to_message_id:
            data['reply_to_message_id']=reply_to_message_id
        if allow_sending_without_reply:
            data['allow_sending_without_reply']=allow_sending_without_reply
        if reply_markup:
            data['reply_markup']=shitgram.utils.reply_markup_parse(reply_markup)

        if is_file:
            resp_json = await self.sendRequest(
                method_name="sendAudio",
                params=data,
                timeout=timeout,
                files={"voice": voice}
            )
        else:
            resp_json = await self.sendRequest(
                method_name="sendAudio",
                params=data,
                timeout=timeout
            )
        return shitgram.types.Update()._parse(shitgram.types.Message()._parse(resp_json.get("result")))