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
        data = {
            'chat_id': chat_id,
            'from_chat_id': from_chat_id,
            'message_id': message_id
        }
        if message_thread_id:
            data['message_thread_id']=message_thread_id
        if parse_mode:
            data['parse_mode']=parse_mode
        if caption:
            data['caption']=caption
        if caption_entities:
            data['caption_entities']=dumps([i.__dict__.get("_dtc__dict") for i in caption_entities], ensure_ascii=False)
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

        resp_json = await self.sendRequest(
            method_name="copyMessage",
            params=data,
            timeout=timeout
        )
        if not resp_json.get("ok"):
            raise shitgram.exceptions.ApiException(
                dumps(resp_json, ensure_ascii=False)
            )
        return shitgram.types.Update()._parse(shitgram.types.Message()._parse(resp_json.get("result")))