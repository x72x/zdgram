from typing import Union

import zdgram

class SendVideoNote:
    async def sendVideoNote(
            self: "zdgram.Bot",
            chat_id: Union[int, str],
            video_note: Union["zdgram.types.InputFile", str, bytes],
            duration: int = None,
            length: int = None,
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
        As of v.4.0, Telegram clients support rounded square MPEG4 videos of up to 1 minute long. Use this method to send video messages. On success, the sent Message is returned.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param video_note: Video note to send. Pass a file_id as String to send a video note that exists on the Telegram servers (recommended) or upload a new video using multipart/form-data
        :param duration: Duration of sent video in seconds
        :param length: Video width and height, i.e. diameter of the video message
        :param thumbnail: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>
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
        if isinstance(video_note, str):
            data['video_note']=video_note
        elif isinstance(video_note, zdgram.types.InputFile):
            is_file = True
        elif isinstance(video_note, bytes):
            is_file = True
        if self.protect_content:
            data['protect_content']=self.protect_content
        if self.disable_notification:
            data['disable_notification']=self.disable_notification
        if duration:
            data["duration"]=duration
        if length:
            data["length"]=length
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
            files["video_note"]=video_note
            if thumbnail:
                files["thumbnail"]=thumbnail
            resp_json = await self.sendRequest(
                method_name="sendVideoNote",
                params=data,
                timeout=timeout,
                files=files
            )
        else:
            resp_json = await self.sendRequest(
                method_name="sendVideoNote",
                params=data,
                timeout=timeout
            )
        return zdgram.bot.update_manager._parse(zdgram.bot.message_manager._parse(resp_json.get("result")))

    send_video_note = sendVideoNote