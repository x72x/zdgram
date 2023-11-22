from typing import Union

import zdgram

class SendSticker:
    async def sendSticker(
            self: "zdgram.Bot",
            chat_id: Union[int, str],
            sticker: Union["zdgram.types.InputFile", str, bytes],
            emoji: str = None,
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
        Use this method to send static .WEBP, animated .TGS, or video .WEBM stickers. On success, the sent Message is returned.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param sticker: Sticker to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a .WEBP sticker from the Internet, or upload a new .WEBP or .TGS sticker using multipart/form-data. More information on Sending Files: https://core.telegram.org/bots/api#sending-files ». Video stickers can only be sent by a file_id. Animated stickers can't be sent via an HTTP URL.
        :param emoji: Emoji associated with the sticker; only for just uploaded stickers
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
        if isinstance(sticker, str):
            data['sticker']=sticker
        elif isinstance(sticker, zdgram.types.InputFile):
            is_file = True
        elif isinstance(sticker, bytes):
            is_file = True
        if self.protect_content:
            data['protect_content']=self.protect_content
        if self.disable_notification:
            data['disable_notification']=self.disable_notification
        if message_thread_id:
            data['message_thread_id']=message_thread_id
        if emoji:
            data['emoji']=emoji
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
                method_name="sendSticker",
                params=data,
                timeout=timeout,
                files={
                    "sticker": sticker
                }
            )
        else:
            resp_json = await self.sendRequest(
                method_name="sendSticker",
                params=data,
                timeout=timeout
            )
        return zdgram.bot.update_manager._parse(zdgram.bot.message_manager._parse(resp_json.get("result")))

    send_sticker = sendSticker