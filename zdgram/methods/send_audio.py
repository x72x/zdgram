from orjson import dumps
from typing import Union, List

import zdgram

class SendAudio:
    async def sendAudio(
            self: "zdgram.Bot",
            chat_id: Union[int, str],
            audio: Union["zdgram.types.InputFile", str, bytes],
            caption: str = None,
            parse_mode: str = None,
            caption_entities: List["zdgram.types.MessageEntity"] = None,
            duration: int = None,
            performer: str = None,
            title: str = None,
            thumbnail: Union["zdgram.types.InputFile", str] = None,
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
        Use this method to send audio files, if you want Telegram clients to display them in the music player. Your audio must be in the .MP3 or .M4A format. On success, the sent Message is returned. Bots can currently send audio files of up to 50 MB in size, this limit may be changed in the future.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param audio: Audio file to send. Pass a file_id as String to send an audio file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get an audio file from the Internet, or upload a new one using multipart/form-data. More information on Sending Files » https://core.telegram.org/bots/api#sending-files
        :param caption: Audio caption, 0-1024 characters after entities parsing
        :param parse_mode: Mode for parsing entities in the audio caption. See formatting options for more details.
        :param caption_entities: A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode
        :param duration: Duration of the audio in seconds
        :param performer: Performer
        :param title: Track name
        :param thumbnail: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files » https://core.telegram.org/bots/api#sending-files
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
        files = {}
        is_file = False
        if isinstance(audio, str):
            data['audio']=audio
        elif isinstance(audio, zdgram.types.InputFile):
            is_file = True
        elif isinstance(audio, bytes):
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
                data['caption_entities']=dumps([i.__default__(i) for i in caption_entities]).decode()
            else:
                data['caption_entities']=dumps([i.__default__(i) for i in caption_entities]).decode()
        if duration:
            data["duration"]=duration
        if performer:
            data["performer"]=performer
        if title:
            data["title"]=title
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
            files["audio"]=audio
            if thumbnail:
                files["thumbnail"]=thumbnail
            resp_json = await self.sendRequest(
                method_name="sendAudio",
                params=data,
                timeout=timeout,
                files=files
            )
        else:
            resp_json = await self.sendRequest(
                method_name="sendAudio",
                params=data,
                timeout=timeout
            )
        return zdgram.bot.update_manager._parse(zdgram.bot.message_manager._parse(resp_json.get("result")))

    send_audio = sendAudio